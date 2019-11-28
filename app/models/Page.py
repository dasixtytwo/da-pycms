from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField,
    IntField
)
import datetime


class Page(Document):
    name = StringField(max_length=200)
    slug = StringField(max_length=200)
    content = StringField()
    template = StringField(max_length=200)
    is_startpage = BooleanField(default=False)
    order = IntField(default=0)
    created_at = DateTimeField(default=datetime.datetime.now())
    data = DictField()
    fields = DictField()

    def get_field(self, name):
        for k, v in self.fields.items():
            realname = k.split('template-field_')[1]

            if name == realname:
                return v
