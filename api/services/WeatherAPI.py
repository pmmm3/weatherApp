import json
import requests
import datetime as dt
from flask import Response, jsonify
from api.schemes.city_schema import CitySchema


class WeatherAPI:
    key = "496a179d6bc08d2cca86e508d1d50c6f"

    def search(name):
        try:
            file = open(f'../bd/{name}.json')
            data = json.load(file)
            file.close()
            return data
        except:
            return None

    def store(name, data):

        try:
            file = open(f'../bd/{name}.json', 'w')
            json_string = json.dumps(data)
            file.write(json_string)
            file.close()
        except:
            raise('No se ha podido guardar el documento')

    def get_city(city_id):
        str(city_id)
        # Search city in bd
        bd_id = WeatherAPI.search(city_id)
        if ((bd_id is not None) and
            (bd_id['created'] - dt.datetime.now()) < dt.timedelta(minutes=10)):
            # exist and  it's updated
            # openweathermap actualize data every 10 minutes
            print("Not implent yet")
        else:
            # Make the openweathermap api call

            url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={WeatherAPI.key}'
            response = requests.get(url).json()
            if response['cod'] == 200:
                schema = CitySchema()
                c_id = str(response['id'])
                lat = response['coord']['lat']
                lon = response['coord']['lon']
                city_data = {
                    "city_id": c_id,
                    "lat": lat,
                    "lon": lon
                }
                result = schema.dump(city_data)
                return json.dumps({'message': result, 'cod': 200})
            else:
                return json.dumps({'message': None, 'cod': 404})

    def get_cities(cities):
        cities = str(cities).split(",")
        total = []
        for id_c in cities:
            result = WeatherAPI.get_city(id_c)
            total.append(json.loads(result)['message'])
        return json.dumps(total)

