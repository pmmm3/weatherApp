from urllib import response
from flask import Response, abort
from flask_smorest import Blueprint
from api.schemes.historical_schema import HistoricalSchema

from api.schemes.info_schema import InfoWeatherSchema
from ..services.WeatherAPI import WeatherAPI as api
city = Blueprint('city', __name__)


@city.route('/city/<city_id>')
@city.response(200, InfoWeatherSchema)
def get_city(city_id):
    response =  api.get_city(city_id)
    if response['cod'] == '404':
        abort(404,'Not found')
    elif response['cod'] == 200:
        return response

# cities ids examples : 2172797,833,2960
@city.route('/cities/<cities_ids>')
@city.response(200, InfoWeatherSchema(many=True))
def get_cities(cities_ids):
    return api.get_cities(cities_ids)

@city.route('/historical/<cities_ids>')
@city.response(200, HistoricalSchema(many=True))
def get_historical(cities_ids):
    return api.get_historical(cities_ids)
