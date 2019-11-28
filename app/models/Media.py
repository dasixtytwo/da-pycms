from mongoengine import (
    Document,
    StringField,
    DateTimeField
)
import datetime


class Media(Document):
    name = StringField(max_length=200)
    filename = StringField()
    created_at = DateTimeField(default=datetime.datetime.now())
