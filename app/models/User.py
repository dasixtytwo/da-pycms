from mongoengine import (
    Document, 
    StringField, 
    ReferenceField
)
from app.models.Media import Media


class User(Document):
    name = StringField(max_length=120, unique=True)
    password = StringField(min_length=5)
    role = StringField(default='Administrator')
    avatar = ReferenceField(Media)
