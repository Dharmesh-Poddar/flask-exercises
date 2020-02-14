from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 
import os

app=Flask(__name__)
Bootstrap(app)
app.secret_key="SECRET KEY"

basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'

db=SQLAlchemy(app)

class Data(db.Model):
	 id= db.Column(db.Integer,primary_key=True)
	 name= db.Column(db.String(100))
	 email= db.Column(db.String(100))
	 phone= db.Column(db.String(100))

def __init__(self,name,email,phone):
     self.name= name
     self.email= email
     self.phone= phone



@app.route('/')
def index():
	return render_template('index.html')


if __name__=='__main__':
	app.run(debug='True')
