import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mnt/C:/Users/Dharmesh/Desktop/flaskExercises/multipledatabase/one.db'
app.config['SQLALCHEMY_BINDS']={ 'two' : 'sqlite:///mnt/C:/Users/Dharmesh/Desktop/flaskExercises/multipledatabase/two.db',
                                 'three': 'sqlite:///mnt/C:/Users/Dharmesh/Desktop/flaskExercises/multipledatabase/three.db'}


db=SQLAlchemy(app)

class One(db.Model):
    id= db.Column(db.Integer, primary_key= True)

class Two(db.Model):
	__bind_key__=='two'
	id = db.Column(db.Integer, primary_key=True)

class Three(db.Model):
	__bind_key__=='three'
	id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    second= Two(id=634)
    db.session.add(second)
    db.session.commit()

    return 'added a value to the second table'


if __name__=='main':
	app.run(debug='True')