from mongoengine import (
  Document,
  StringField,
  DateTimeField
)
import datetime


class Group(Document):
  name = StringField(max_length=100)
  description=StringField(max_length=200)
  created_at = DateTimeField(default=datetime.datetime.now())