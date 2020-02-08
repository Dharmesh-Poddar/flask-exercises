from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
	file= request.files['inputfile']
	return file.filename

if __name__=='main':
	app.run(debug='True')
