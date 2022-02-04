import datetime as dt
from marshmallow import Schema, ValidationError, fields, post_load, validates


class City:
    def __init__(self, city_id, lat, lon):
        self.city_id = city_id
        self.lat = lat
        self.lon = lon
        self.created_at = dt.datetime.now()



class CitySchema(Schema):
    city_id = fields.Str()
    lat = fields.Float()
    lon = fields.Float()
    created_at = fields.DateTime(default=dt.datetime.now())

    @validates("city_id")
    def validate_id(self, value):
        if len(value) <= 1:
            raise ValidationError("city id must be greater than 0.")

#    @post_load
#    def make_user(self, data, **kwargs):
#        return City(**data)
