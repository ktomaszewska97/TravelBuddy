from datetime import datetime

from marshmallow import Schema, ValidationError, fields, validates
from marshmallow.validate import Length


class ProfileSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    mobile = fields.String()
    date_of_birth = fields.Date()
    country = fields.String()
    if_english = fields.Boolean()
    about = fields.String()

    @validates("date_of_birth")
    def is_not_in_future(value):
        now = datetime.now()
        if value > now:
            raise ValidationError("Date can't be in the future!")


class UserSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    profile_id = fields.Nested(ProfileSchema)


class TripSchema(Schema):
    id = fields.Integer(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    trip_title = fields.String(required=True, validate=Length(max=100))
    gender = fields.Integer()
    type_of_trip = fields.String(required=True, validate=Length(max=50))
    housing = fields.String(required=True, validate=Length(max=50))
    food = fields.String(required=True, validate=Length(max=50))
    budget = fields.Integer()
    must_do = fields.String(validate=Length(max=255))
    must_see = fields.String(validate=Length(max=255))
    owner_id = fields.Nested(UserSchema)

    @validates("start_date")
    def is_not_in_future(value):
        now = datetime.now()
        if value > now:
            raise ValidationError("Date can't be in the future!")

    @validates("end_date")
    def is_not_in_future(value):
        now = datetime.now()
        if value > now:
            raise ValidationError("Date can't be in the future!")


class PlaceSchema(Schema):
    id = fields.Integer(required=True)
    place_name = fields.String(required=True, validate=Length(max=255))
    trip_id = fields.Nested(TripSchema)


class FavouriteSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Nested(UserSchema)
    trip_id = fields.Nested(TripSchema)


class ActivitySchema(Schema):
    id = fields.Integer(required=True)
    activity_name = fields.String(required=True, validate=Length(max=255))
    trip_id = fields.Nested(TripSchema)
