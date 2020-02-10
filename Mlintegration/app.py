from flask import Flask,request,render_template
from predictor_api import make_prediction


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def predict():
	print(request.args)
	 if(request.args):
        x_input, predictions = \
            make_prediction(request.args['chat_in'])
        print(x_input)
        return flask.render_template('predictor.html',
                                     chat_in=x_input,
                                     prediction=predictions)
 	
     else:
     	x_input,predictions=make_prediction('')
     	return render_template('predictor.html',chat_in=x_input,prediction=predictions)
     	



@app.route('/')
def predict():
	return render_template('')

if __name__=='__main__':
	app.run(debug='True')
