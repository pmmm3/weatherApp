import datetime as dt
from email.policy import default
from marshmallow import Schema, ValidationError, fields, post_load, validates


class Temperature:
    def __init__(self, temp, temp_min=None, temp_max = None):
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max


class TemperatureSchema(Schema):
    temp = fields.Float(required = True)
    temp_min = fields.Float(default = None)
    temp_max = fields.Float(default= None)
    @validates("temp_min")
    def validate_temp_min(self, value):
        if (value is not None):
            if(value > self.temp_max):
                raise ValidationError ("temperaure min can not be greater than max")
    @validates("temp_max")
    def temp_max(self, value):
        if (value is not None):
            if(value < self.temp_min):
                raise ValidationError(
                    "temperaure min can not be greater than max")

    @post_load
    def make_Temperature(self, data, **kwargs):
        return Temperature(**data)
