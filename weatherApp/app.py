import requests
from flask import Flask,render_template 
app = Flask(__name__)

@app.route('/')
def index():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=4d5e7c1a2cd8f2338eb3f0d0b21ce3b0'
    city='las vegas'

    r=request.get(url.format(city)).json()
    print(r)
    return render_template('weather.html')
    
if __name__=='__main__':
    app.run(debug='True')



