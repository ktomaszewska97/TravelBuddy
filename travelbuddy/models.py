from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy_utils import ChoiceType

from app import db, login

GENDER = [("man", "Man"), ("woman", "Woman")]

BUDGET = [
    ("small", "<250$"),
    ("medium", "250$-750$"),
    ("regular", "750$-1500$"),
    ("big", "1500$+"),
]

TYPE_OF_TRIP = [
    ("city_break", "City break"),
    ("work_and_travel", "Work&travel"),
    ("roadtrip", "Roadtrip"),
    ("backpacking", "Backpacking"),
    ("vacations", "Vacations"),
    ("other", "Other"),
]

HOUSING = [
    ("camping", "Camping"),
    ("airbnb", "AirBnB"),
    ("couchsurfing", "Couchsurfing"),
    ("hotels", "Hotels"),
    ("hostels", "Hostels"),
    ("other", "Other"),
]

FOOD = [
    ("self", "Self-cooking"),
    ("fastfoods", "Fast foods"),
    ("bistros", "Bistros"),
    ("restaurants", "Restaurants"),
]


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date())
    country = db.Column(db.String(200))
    if_english = db.Column(db.Boolean())
    about = db.Column(db.String(255))
    gender = db.Column(ChoiceType(GENDER))
    user = db.relationship("User", backref="profile", uselist=False)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.id"))
    trips = db.relationship("Trip", backref="owner")
    favourites = db.relationship("Favourite", backref="user")

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Trip(db.Model):
    __tablename__ = "trip"
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    trip_title = db.Column(db.String(100))
    gender = db.Column(ChoiceType(GENDER))
    type_of_trip = db.Column(ChoiceType(TYPE_OF_TRIP))
    housing = db.Column(ChoiceType(HOUSING))
    food = db.Column(ChoiceType(FOOD))
    budget = db.Column(ChoiceType(BUDGET))
    must_do = db.Column(db.String(255))
    must_see = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    places = db.relationship("Place", backref="place")
    favourites = db.relationship("Favourite", backref="trip")
    activities = db.relationship("Activity", backref="trip")


class Place(db.Model):
    __tablename__ = "place"
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(255))
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"))


class Favourite(db.Model):
    __tablename__ = "favourite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"))


class Activity(db.Model):
    __tablename__ = "activity"
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(255))
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"))
