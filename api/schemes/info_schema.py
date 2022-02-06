import datetime as dt
from email.policy import default
from marshmallow import Schema, ValidationError, fields, post_load, validates


class InfoWeather:
    def __init__(self, temperature, pressure, humidity, weather):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.weather = weather


