import os
from flask import Flask 
from flask_sqlalchemy import flask_sqlalchemy

basedir =os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


##################### Model h bhai h aage########

class puppy(db.Model):

	__tablename__='puppies'

	id =db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    age= db.Column(db.Integer)

    def __init__(self,name,age):
          self.name =name 
          self.age = age

    def __repr__(self):
           return f"Puppy {self.name} is {self.age} years old"

           