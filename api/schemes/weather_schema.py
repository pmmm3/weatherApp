import datetime as dt
from marshmallow import Schema, ValidationError, fields, post_load, validates


class Weather:
    def __init__(self, main, description):
        self.main = main
        self.description = description


class WeatherSchema(Schema):
    main = fields.Str()
    description = fields.Str()

    @post_load
    def make_weather(self, data, **kwargs):
        return Weather(**data)
