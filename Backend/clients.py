from flask_restx import Namespace, Resource, fields
import random
import string
import mysql.connector
from models import *
from flask import request



clients_ns = Namespace("clients", description="A namespace for clients")

clients_model = clients_ns.model(
    "Clients",
     {"id": fields.Integer(), "sirName": fields.String(),"fullName": fields.String(), "email": fields.String(),"contactCode": fields.Integer()}
)


@clients_ns.route("/Hello")
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello world"}

@clients_ns.route("/clients", methods = ['GET', 'POST'])
class clientsResource(Resource):
    @clients_ns.marshal_list_with(clients_model) #serializes the sql data returned into a json object
    def get(self):
        """Get all clients"""

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  Clients")
        data = cursor.fetchall()
        return str(data)

    @clients_ns.marshal_with(clients_model)
    @clients_ns.expect(clients_model)
   
    def post(self):
        """Create a new client"""
        cursor = conn.cursor()
        data = request.get_json()

        new_client = client(
        sir_name = data.get("sirName"),name = data.get("fullName"), email = data.get("email"),clientCode = data.get(" "))

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clients(sirName, fullName, email, clientCode) VALUES (%s, %s, %s, %s)", (sirName, fullName, email, clientCode))
        mysql.connection.commit()
        cursor.close()

        return new_client, 201
def generate_code():
    alpha_chars = ''.join(random.choices(string.ascii_uppercase, k=3))
    num_digits = ''.join(random.choices(string.digits, k=3))
    return alpha_chars + num_digits

def save_client(name):
    # Connect to the database
    connection = mysql.connector.connect()
    cursor = conn.cursor()
    
    # Generate unique code
    code = generate_code()
    while True:
        # Check if the code already exists in the database
        query = "SELECT COUNT(*) FROM Clients WHERE clientCode = %s"
        cursor.execute(query, (code,))
        result = cursor.fetchone()
        if result[0] == 0:
            # Code does not exist, break out of the loop
            break
        # Code exists, generate another code
        code = generate_code()
    
    # Save the client to the database
    query = "INSERT INTO Clients (name, clientCode) VALUES (%s, %s)"
    cursor.execute(query, (name, clientCode))
    connection.commit()
    
    # Return the generated code
    return code

@clients_ns.route("/clients", methods=["GET", "PUT"])   
class clientsResource(Resource):
    @clients_ns.marshal_with(clients_model)
    def get_linked_contacts(self, id):
        """Get a client by id"""
        # Create a cursor object to execute SQL commands
        cursor = db.cursor()
        # Execute the SQL query to count the number of linked contacts
        query = "SELECT COUNT(*) FROM contacts WHERE client_id IS NOT NULL"
        cursor.execute(query)
        # Fetch the result of the query
        result = cursor.fetchone()
        # Print the number of linked contacts
        print("Number of linked contacts:", result[0])
        return result
        # Close the cursor and the database connection
        cursor.close()
        db.close()

    
    '''@clients_ns.marshal_with(clients_model)
    def put(self, id):
        """Update a client by id"""

        client_to_update = Clients.query.get(id)

        data = request.get_json()

        client_to_update.update(sir_name = data.get("sir_name"),name = data.get("name"), email = data.get("email"),client_code = data.get("client_code"))

        return client_to_update

   
    @clients_ns.marshal_with(clients_model)
    def delete(self, id):
        """Delete a client by id"""

        client_to_delete = Clients.query.get_or_404(id)

        client_to_delete.delete()

        return client_to_delete'''