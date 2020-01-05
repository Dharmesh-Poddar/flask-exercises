from flask import flask
from flask_restful import Api,Resource

app=flask(__name__)
api=Api(app)

puppies=[]

class PuppyNames(Resource):
	def GET(self,name):
		for pup in puppies:
			if pup['name']==name:
				return pup
    
        return {'name':none}

     
     


if __name__=='__main__':
	app.run(debug=True)