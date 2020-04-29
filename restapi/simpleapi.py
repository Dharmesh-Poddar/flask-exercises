from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

class Add(Resource):
    def post(self): 
        postedData= request.get_json()
        x=postedData["x"]
        y=postedData["y"]
        ret=x+y
        retMap={
           'Message': ret,
           'status code': 200

        }
        return jsonify(retMap)

class Sub(Resource):
    def post(self): 
        postedData= request.get_json()
        x=postedData["x"]
        y=postedData["y"]
        ret=x-y
        retMap={
           'Message': ret,
           'status code': 200

        }
        return jsonify(retMap)


api.add_resource(Add,'/add')
api.add_resource(Sub,'/sub')



@app.route('/')
def hello_world():
	return "hello_world"

if __name__=='__main__':
	app.run(debug='True')
