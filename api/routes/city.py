from flask import Blueprint
from ..services.WeatherAPI import WeatherAPI as api
city = Blueprint('city', __name__)


@city.route('/city/<city_id>')
def get_city(city_id):
    return api.get_city(city_id)
# cities ids examples : 2172797,833,2960
@city.route('/cities/<cities_ids>')
def get_cities(cities_ids):
    return api.get_cities(cities_ids)
