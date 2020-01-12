import os
from flask import Flask 
from flask_sqlalchemy import Flask_SQLAlchemy 
from flask_migrate import Migrate 
from flask_login import LoginManager


app = Flask(__name__)

############################
######Database part##########
#############################

basedir =os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 


db=SQLAlchemy(app)
Migrate(app,db)


from socialcompany.core.views import core
from socialcompany.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
