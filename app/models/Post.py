from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField,
    ListField,
    ReferenceField
)
import datetime


class Post(Document):
    title = StringField(max_length=200)
    slug = StringField(max_length=200)
    content = StringField()
    template = StringField(max_length=200)
    is_published = BooleanField(default=True)
    group = StringField(max_length=150)
    medias = ListField(ReferenceField('Media'))
    created_at = DateTimeField(default=datetime.datetime.now())
    with_sidebar = BooleanField(default=False)
    data = DictField()
    fields = DictField()

    def get_field(self, name):
        for k, v in self.fields.items():
            # name = k.split('post-tmpl-field_')[1]
            realname = k.split('post-tmpl-field_')[1]

            if name == realname:
                return v
