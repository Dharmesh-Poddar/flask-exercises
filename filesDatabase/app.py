from flask import Flask,render_template,request
from flask_sqlalchemy import FLASK_SQLAlchemy 

app=Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
db= SQLAlchemy(app)

class addfiles(db.Model):
	 id= db.Column(db.Integer,primary_key='True')
	 name=db.Column(db.string(300))
     data= db.Column(db.LargeBinary)





@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
	file= request.files['inputfile']
	  
	myfile= addfiles(name=inputfile,data=file)
    db.session.add()
    db.session.commit()    
	return "file got added successfully" 

if __name__=='main':
	app.run(debug='True')
