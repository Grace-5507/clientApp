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






