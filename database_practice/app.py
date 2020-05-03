import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

basedir= os.path.abspath(os.path.dirname(__file__))

app= Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

db= SQLAlchemy(app)

######

class Rajasthan(db.Model):
	__tablename__ ='Rajputana'
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.Text)
	age= db.Column(db.Text)


	def __init__(self,id,name,age):
		self.id= id
		self.name= name
        self.age= age 

    