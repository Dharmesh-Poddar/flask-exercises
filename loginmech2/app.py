from flask import Flask,render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap 
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validator import InputRequired,Email,Length


app=flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


if __name__=='main':
	app.run(debug='True')