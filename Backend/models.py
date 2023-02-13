import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="myclient"
    )
cursor = mydb.cursor()

# Create the clients and contacts tables

cursor.execute("CREATE TABLE IF NOT EXISTS clients (client_id INT AUTO_INCREMENT PRIMARY KEY, sirName VARCHAR(255) NOT NULL, fullName VARCHAR(255) NOT NULL, email VARCHAR(255), clientCode VARCHAR(255) NOT NULL)");




cursor.execute("CREATE TABLE IF NOT EXISTS Contacts (contact_id INT AUTO_INCREMENT PRIMARY KEY, sirName VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, client_id INT NOT NULL, FOREIGN KEY (client_id) REFERENCES clients(client_id))");

##cursor.execute("ALTER TABLE Contacts ALTER COLUMN client_id SET DEFAULT 1")
#mydb.commit()
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






'''# Insert a new client into the Clients table
insert_client_sql = "INSERT INTO clients (sirName, fullName, email) VALUES (%s, %s, %s, %s"
cursor.execute(insert_client_sql, (('Johnson', 'Jane Johnson', 'jane.johnson@example.com',  mycode)))
client_id = cursor.lastrowid

# Insert a new contact into the Contacts table
insert_contact_sql = "INSERT INTO Contacts (sirName, name, email, client_id) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_contact_sql, ('Jones', 'Mark Jones', 'mark.jones@example.com', client_id))

# Commit the changes to the database
mydb.commit()'''








