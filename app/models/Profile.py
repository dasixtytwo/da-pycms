from mongoengine import (
  Document,
  StringField,
  ReferenceField
)
from app.models.User import User

class Profile(Document):
  firstName = StringField(max_length=50)
  lastName = StringField(max_length=50)
  email = StringField(max_length=120, unique=True)
  phone = StringField(max_length=30)
  website = StringField(max_length=100)
  address = StringField(max_length=100)
  city = StringField(max_length=100)
  country = StringField(max_length=100)
  postcode = StringField(max_length=100)
  userID = ReferenceField(User)