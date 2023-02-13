import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="client"
)
cursor = conn.cursor()

'''# Create the clients and contacts tables

CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    sirName VARCHAR(255) NOT NULL,
    fullName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    clientCode VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS Contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    sirName VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    client_id INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);
'''

'''cursor.execute(clients_table)
cursor.execute(contacts_table)
conn.commit()'''

# Add a client to the clients table
def add_client(name, email):
    sql = "INSERT INTO clients (client_name, client_email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    conn.commit()
    print("Client added successfully")

# Add a contact to the contacts table
def add_contact(name, email, client_id):
    sql = "INSERT INTO Clients(sirName, fullName, email, clientCode) VALUES (%s, %s, %s, %s)"
    values = (sirName, fullName, email, clientCode)
    cursor.execute(sql, values)
    conn.commit()
    print("Contact added successfully")

# Link a client to a contact
def link_client_to_contact(client_id, contact_id):
    sql = "UPDATE contacts SET client_id=%s WHERE contact_id=%s"
    values = (client_id, contact_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Client and contact linked successfully")


