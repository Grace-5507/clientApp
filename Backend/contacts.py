from flask_restx import Namespace, Resource, fields
from models import *




contacts_ns = Namespace("contacts", description="A namespace for contacts")

contacts_model = contacts_ns.model(
    "Contacts",
 {"contact_id": fields.Integer(), "sirName": fields.String(),"name": fields.String(), "email": fields.String(),"client_id": fields.Integer() }
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

        cursor = mydb.cursor()
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

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Contacts(sirName, name, email) VALUES (%s, %s, %s)", (sirName, name,email))
        mydb.commit()
        cursor.close()

        return new_contact, 201
    
    
    
    
linked_contacts_ns = Namespace("linked_contacts", description="A namespace for linked_contacts")

linked_contacts_model = linked_contacts_ns.model('LinkedContacts', {
    'linked_contacts': fields.Integer
})

@linked_contacts_ns.route('/linked_contacts')
class LinkedContactsResource(Resource):
    @linked_contacts_ns.marshal_with(linked_contacts_model)
    def get(self):
        """Get number of linked contacts"""
        # Connect to the database
        # Connect to the database
        mydb()
    
        # Create a cursor object to execute SQL commands
        cursor = mydb.cursor()
        # Execute the SQL query to count the number of linked contacts
        query = "SELECT COUNT(*) FROM contacts WHERE client_id IS NOT NULL"
        cursor.execute(query)
        # Fetch the result of the query
        result = cursor.fetchone()
        # Store the number of linked contacts
        linked_contacts = result[0]
        # Close the cursor and the database connection
        cursor.close()
        db.close()
        # Return the number of linked contacts
        return {'linked_contacts': linked_contacts}




       
        
        
        
        
        
        
        
        
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