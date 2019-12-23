#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class RegisterationForm(FlaskForm):
	 email= StringField('Email',validators=[DataRequired(),Email()])
	 username= StringField('Username',validators=[DataRequired()])
	 password= PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
	 pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
	 submit =SubmitField('Register!')

	 