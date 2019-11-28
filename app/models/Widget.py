from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField,
    IntField
)
import datetime


class Widget(Document):
    title = StringField(max_length=50)
    subtitle = StringField(max_length=50)
    date_start = StringField(max_length=10)
    date_end = StringField(max_length=10)
    icon = StringField()
    content = StringField()
    page = StringField()
