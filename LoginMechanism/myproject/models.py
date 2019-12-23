from myproject import db,login_manger
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
	__tablename__='users'
	