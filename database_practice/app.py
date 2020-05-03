import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

basedir= os.path.abspath(os.path.dirname(__file__))

app= Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db= SQLAlchemy(app)

######

class Rajasthan(db.Model):
	__tablename__ ='Rajputana'

	id = db.Column(db.Integer, primary_key=True)
	distname = db.Column(db.Text)
	famous = db.Column(db.Text)


	def __init__(self,id,distname,famous):
		self.id= id
		self.distname= distname 
		self.famous= famous
        
    
