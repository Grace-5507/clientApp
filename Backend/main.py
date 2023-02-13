from flask import Flask
from flask_restx import Api #Flask_restx provides a coherent collection of decorators and tools to describe  API and expose its documentation properly (using Swagger).
from contacts import contacts_ns
from clients import clients_ns
from flask_mysqldb import MySQL
from flask_cors import CORS
from models import *


app=Flask(__name__)
CORS(app) #configuring api to work with the client application
mysql = MySQL(app)
    

api=Api(app, doc="/docs")
    

api.add_namespace(contacts_ns)
api.add_namespace(clients_ns)


    
  
if __name__ == '__main__':
    
    app.debug = True
    app.run()








'''CREATE TABLE Contacts(id   INT unsigned NOT NULL AUTO_INCREMENT, sirName VARCHAR(150) NOT NULL,            name VARCHAR(150) NOT NULL, email VARCHAR(150) NOT NULL,  PRIMARY KEY     (id)                                  
 );'''

'''INSERT INTO Clients ( sirName, fullName, email, clientCode ) VALUES( 'Sandy', 'Lennon Opiyo', 'sandy@yahoo.com', ' '),( 'Cookie', 'Casey Ochieng', 'cookie@gmail.com', " " ),( 'Charlie', 'River Onyango', 'charlier@hotmail.com', " " ),( 'Seth', 'Maha Ooyo', 'seth@yahoo.com', " "),( 'Caleb', 'Chaer Okoth', 'okothe@gmail.com', " " ),( 'June', 'Yambo Ochieng', 'june@hotmail.com', " " ),( 'Charity', 'Rodger Onyango', 'rodger@hotmail.com', " " ),( 'Stacy', 'Maharia Ochieng', 'stacy@yahoo.com', " " ),( 'Channel', 'Cathye James', 'cathye@gmail.com', " " );

INSERT INTO Contacts ( sirName, name, email) VALUES( 'James', 'Leny', 'james@gmail.com' ),( 'John', 'Casey', 'john@gmail.com' ),( 'Jacob', 'Kutwa', 'jacob@gmail.com' ),('Janet' , 'Smith', 'janet@gmail.com'),('June' , 'Smiley', 'june@gmail.com'),('Jackline' , 'Oyoo', 'jackline@gmail.com');'''