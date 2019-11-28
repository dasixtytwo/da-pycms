from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextField,
    TextAreaField,
    HiddenField,
    SubmitField,
    ValidationError
)
from wtforms.validators import (
    Required,
    Length,
    Email
)


class ContactMailSettingsForm(FlaskForm):
    name = StringField('Name', validators=[Required("Please enter your name, min length 3 characters."), Length(min=3, max=120)], render_kw={
                       "placeholder": "Your Name..."})
    email = TextField("Email", validators=[Required("Please enter your email address."), Email("Please enter your email address.")], render_kw={
                      "placeholder": "Your Email..."})
    subject = HiddenField("Subject")
    message = TextAreaField("Message", validators=[Required("Please enter a message, min length 4 characters."), Length(min=4, max=120)], render_kw={
                            "placeholder": "Your Message...", "cols": "45", "rows": "5"})
    submit = SubmitField("say hello!")
