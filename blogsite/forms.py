# File containing forms for blogsite

from flask_wtf import FlaskForm
from wtforms import validators, fields


class LoginForm(FlaskForm):
    username = fields.StringField('Username', validators=[validators.DataRequired(), validators.Length(min=8, max=64)])
    password = fields.PasswordField('Password', validators=[validators.DataRequired(), validators.Length(min=8, max=64)])
    submit = fields.SubmitField('Sign In')
