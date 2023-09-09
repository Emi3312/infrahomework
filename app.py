from flask import Flask
import requests
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

API_KEY = "c4e0c00323814af9a3307fb398ebae43"

@app.route('/')
def index():
    return 'App Funcionando!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = dict(
        q=city + "," + country,
	    units='metric',
        appid= API_KEY,
    ) 

    response = requests.get(url=url, params=params)
    data = response.json()
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)