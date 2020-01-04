from flask import Flask,render_template
from flask_sqlalchemy import SQL_Alchemy


basedir =os.path.abspath(os.path.dirname(__file__))
app =Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post')
def post():
	 return render_template('post.html')

@app.route('/add')
def add():
	return render_template('add.html')




if __name__=='__main__':
  app.run(debug='True')