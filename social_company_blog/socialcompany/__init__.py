from flask import Flask 

app = Flask(__name__)

from socialcompany.core.views import core

app.register_blueprint(core)
