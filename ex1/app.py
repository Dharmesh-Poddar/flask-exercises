from flask import Flask ,render_template, request
app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signup_form')
def signup_form():
	return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
   first =request.args.get('first')
   last =request.args.get('last')
   return render_template('thankyou.html',first=first,last=last)


if __name__=='main':
	app.run(debug=True)
