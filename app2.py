from flask import Flask
import requests

app = Flask(__name__)


API_KEY = "c4e0c00323814af9a3307fb398ebae43"

@app.route('/')
def index():
    return 'App Funcionando!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):
    query= city + ',' + country
    api= API_KEY
    url = 'https://samples.openweathermap.org/data/2.5/weather?q='+query+'&appid='+api

    #url = "https://samples.openweathermap.org/data/2.5/weather"
    #params = dict(
    #    q=city + "," + country,
    #    appid= API_KEY,
    #) 

    #response = requests.get(url=url, params=params)
    ##response = requests.get(url=url)
    #data = response.json()
    return query + '-' + api + '-' + url
    #return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)