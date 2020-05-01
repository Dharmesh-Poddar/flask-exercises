import os
from flask import Flask,request
import requests
from flask_sqlalchemy import SQLAlchemy 

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')

db= SQLAlchemy(app)





if __name__=='__main__':
	app.run(debug=True)
	