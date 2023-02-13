from flask_restx import Namespace, Resource, fields




contacts_ns = Namespace("contacts", description="A namespace for contacts")

contacts_model = contacts_ns.model(
    "Contacts",
 {"id": fields.Integer(), "sirName": fields.String(),"name": fields.String(), "email": fields.String()}
)

@contacts_ns.route("/Hello")
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello world"}

@contacts_ns.route("/contacts", methods = ['GET', 'POST'])
class contactsResource(Resource):
    @contacts_ns.marshal_list_with(contacts_model) #serializes the sql data returned into a json object
    def get(self):
        """Get all contacts"""

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM  Contacts")
        data = cursor.fetchall()
        return str(data)

    @contacts_ns.marshal_with(contacts_model)
    @contacts_ns.expect(contacts_model)
   
    def post(self):
        """Create a new contact"""

        data = request.get_json()

        new_contact = contacts(
        sir_name = data.get("sirName"),name = data.get("name"), email = data.get("email"))

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Contacts(sirName, name, email) VALUES (%s, %s, %s)", (sirName, name,email))
        mysql.connection.commit()
        cursor.close()

        return new_contact, 201
    
    
    
    
@contacts_ns.route("/linked_contacts", methods=["GET"])   
class contactsResource(Resource):
    @contacts_ns.marshal_with(contacts_model)
    def get_linked_clients(self, id):
        """Get a linked_clients"""
        # Create a cursor to execute queries
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM clients WHERE contact_id IS NOT NULL"
        cursor.execute(query)
        # Fetch the result of the query
        result = cursor.fetchone()
       # Extract the count from the result
        count = result[0]

        # Print the count of linked clients
        print("Number of linked clients:", count)
        return count
        # Close the cursor and the database connection
        cursor.close()
        cnx.close()
        
        
        
        
        
        
        
        
    '''@contacts_ns.marshal_with(contacts_model)
    def put(self, id):
        """Update a contact by id"""

        contact_to_update = Contacts.query.get(id)

        data = request.get_json()

        contact_to_update.update(sir_name = data.get("sir_name"),name = data.get("name"), email = data.get("email"))

        return contact_to_update

   
    @contacts_ns.marshal_with(contacts_model)
    def delete(self, id):
        """Delete a contact by id"""

        contact_to_delete = Contacts.query.get_or_404(id)

        contact_to_delete.delete()

        return contact_to_delete'''