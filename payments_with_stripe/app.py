from flask import Flask ,render_template,request,url_for
import os
import stripe

app= Flask(__name__)

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']


@app.route('/')
   def index():
       return render_template('index.html',public_key=public_key)

@app.route('/thankyou')
   def thankyou():
   	    return render_template('thankyou.html')

@app.route('/payments')
   def payments():
   	     



if __name__='__main__':
	app.run(debug='True')
