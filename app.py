import requests
from flask import Flask ,render_template,request
from flask_sqlalchemy import sqlalchemy

# rename app<=flask
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    city= request.form.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ef1ed6747e01316a94a1483d89e16382'
    req=requests.get(url.format(city)).json()
    
    if 'name' and 'main' and 'weather' in req:
        weather = {
            'name':req['name'],
            'temp': req['main']['temp'] ,
            'temp_max':req['main']['temp_max'],
            'temp_min':req['main']['temp_min'],
            'pressure':req['main']['pressure'],
            'des':req['weather'][0]['description'],
            'icon':req['weather'][0]['icon']
        }
        return render_template('weather.html',weather=weather)
    else:
        msg = req['cod']
        return render_template('weather.html',weather=msg)
    





