import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
basedir =os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////mnt/c:/Users/Dharmesh/Desktop/flaskExercises/sqlalchemy/one.db'		

db=SQLAlchemy(app)

class Example(db.Model):
    __tablename__='example'
    id= db.Column('id',db.Integer,primary_key=True)
    data= db.Column('data',db.Unicode)

    def __init__(self ,id ,data):
    	self.id= id
    	self.data=data