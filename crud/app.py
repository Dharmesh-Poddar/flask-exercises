from flask import flask
from flask_restful import Api,Resource

app=flask(__name__)
api=Api(app)

puppies=[]

class PuppyNames(Resource):
	def get(self,name):
		for pup in puppies:
			if pup['name']==name:
				return pup
        #return {'name':None}

    def post(self,name):
     	pup={'name':name}
     	puppies.append(pup)
     	return pup

    def delete(self,name):
     	 for ind,pup in enumerate(puppies):
     	 	deleted_pup=puppies.pop(ind)
     	 	return {'note':'delete success'}
class AllNames(Resource):
	def(self):
		return {'puppies':puppies}



if __name__=='__main__':
	app.run(debug=True)