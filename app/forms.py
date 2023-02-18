from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

csrf = CSRFProtect()

app = Flask('__name__', template_folder="app/templates/")
app.config['SECRET_KEY'] = '07fdc18061502f867e57b32640708c0181d2077d547ba5f8c1c6d644a9cf3e82'
csrf.init_app(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])