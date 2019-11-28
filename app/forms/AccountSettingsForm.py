from wtforms import (
    Form,
    StringField,
    validators,
    FileField
)


class AccountSettingsForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=120)])
    avatar = FileField('Avatar Image')
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    email = StringField('Email')
    phone = StringField('Phone')
    website = StringField('Website')
    address = StringField('Address')
    city = StringField('City')
    country = StringField('State')
    postcode = StringField('PostCode')
