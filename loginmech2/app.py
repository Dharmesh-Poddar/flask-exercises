from flask import Flask,render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap 
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validator import InputRequired,Email,Length


app=flask(__name__)

app.config['SECRET_KEY']='thisisthesecretkey'

Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8,max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm): 
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=80)])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	form=LoginForm()
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


if __name__=='main':
	app.run(debug='True')
