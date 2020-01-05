from flask import Flask 
from flask_restful import Resource,Api

app =Flask(__name__)
api= Api(app)

class Helloworld(Resource):
	 def get(self):
	 	return {hello:world}

api.add_resource(Helloworld,'/')


if __name__=='main':
	app.run(debug=True)