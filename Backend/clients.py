from flask_restx import Namespace, Resource, fields
import random
import string
import mysql.connector
from models import *
from flask import request



clients_ns = Namespace("clients", description="A namespace for clients")

clients_model = clients_ns.model(
    "Clients",
     {"client_id": fields.Integer(), "sirName": fields.String(),"fullName": fields.String(), "email": fields.String(),"contactCode": fields.Integer()}
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
      
        cursor =mydb.cursor()
        cursor.execute("SELECT * FROM  clients")
        data = cursor.fetchall()
        return str(data)

    @clients_ns.marshal_with(clients_model)
    @clients_ns.expect(clients_model)
   
    def post(self):
        """Create a new client"""
        cursor =mydb.cursor()
        sirName = request.form.get('sirName')
        fullName = request.form.get('fullName')
        clientCode = request.form.get('clientCode')
        email = request.form.get('email')
        
        cursor =mydb.cursor()
        # Insert a new client into the Clients table
       
        
        cursor.execute("INSERT INTO clients(sirName, fullName, email, clientCode) VALUES (%s, %s, %s, %s)", (sirName, fullName, email, clientCode))
        
        client_id = cursor.lastrowid
       

        
        mysql.connection.commit()
        cursor.close()
        return new_client, 201



def generate_code():
    alpha_chars = ''.join(random.choices(string.ascii_uppercase, k=3))
    num_digits = ''.join(random.choices(string.digits, k=3))
    return alpha_chars + num_digits

def save_client(name):

    mydb()
    mydb.corsor()
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

linked_clients_ns = Namespace("linked_clients", description="A namespace for linked_clients")

linked_clients_model = linked_clients_ns.model('Linked_clients', {
    'linked_clients': fields.Integer
})

@linked_clients_ns.route('/linked_clients')
class LinkedclientsResource(Resource):
    @linked_clients_ns.marshal_with(linked_clients_model)
    def get(self):
        """Get number of linked clients"""
        # Connect to the database
        mydb(myclient)
    
        # Create a cursor object to execute SQL commands
        mydb.cursor()
        # Execute the SQL query to count the number of linked clients
        query = "SELECT COUNT(*) FROM clients WHERE client_id IS NOT NULL"
        cursor.execute(query)
        # Fetch the result of the query
        result = cursor.fetchone()
        # Store the number of linked clients
        linked_clients = result[0]
        # Close the cursor and the database connection
        cursor.close()
        db.close()
        # Return the number of linked contacts
        return {'linked_contacts': linked_contacts}




    
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