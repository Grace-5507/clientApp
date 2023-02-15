

Welcome to the Read Me file for my web application built using MySQL, Python, and React. This application is designed to manage clients and contacts for businesses. Below is some information that you may find helpful when using my application.




INSTALLATION
Clone the repository: git clone https://github.com/Grace-5507/studioApp.git
Navigate to the project directory: cd clients
Install the dependencies: npm install
Start the development server: npm start


# Assume you are activating Python 3 venv
$ brew install mysql-client
$ echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
$ export PATH="/usr/local/opt/mysql-client/bin:$PATH"
$ pip install mysqlclient
  pip install flask-mysqldb




Technologies Used
my application uses the following technologies:

MySQL: A relational database management system used to store and manage data.
Python: A high-level programming language used for backend development.
React: A JavaScript library used to build user interfaces.
REST Api


Installation
To install my application, follow these steps:

Clone my repository to my local machine.
Install the necessary dependencies by running npm install in the client directory, and pip install -r requirements.txt in the server directory.
Create a MySQL database and update the connection string in the models.py file in the server directory.
Start the server by running python app.py in the server directory.
Start the client by running npm start in the client directory.
Features
my application allows users to perform the following actions:

Create and  view clients
Create, view, edit contacts associated with clients
Get a list of clients
Get a list of contacts associated with
Get linked coontacts and clients


Database Schema
my database contains two tables:
clients and Contacts

