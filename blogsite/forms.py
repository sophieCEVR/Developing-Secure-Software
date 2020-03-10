# File containing forms for blogsite

from . import models  # Import models for validation
from . import validators  # Import validators for validation (custom validators, NOT builtin wtforms.validators)
from flask_wtf import FlaskForm
from wtforms import fields


class CreateAccountForm(FlaskForm):
    username = fields.StringField('Username*:', validators=[
        validators.Required(),
        validators.AlphaNumeric(),
        validators.Length(min_length=8, max_length=models.User.username.type.length),
        validators.NotContainAny([' ', '_', '&', '<', '>', '/', '\\', "'", '"', ',', '.', '=', '-', '+'])
    ])
    password = fields.PasswordField('Password*:', validators=[
        validators.Required(),
        validators.AlphaNumeric(),
        validators.Length(min_length=8, max_length=models.User.password.type.length),
        validators.NotContainAny([' '], message=u'Field must not contain any spaces'),
        validators.DifferentFrom('username')
    ])
    passwordConfirm = fields.PasswordField('Confirm Password*:', validators=[
        validators.Required(),
        validators.EqualTo('password')
    ])
    captcha = fields.StringField('Complete the sum: ', validators=[
        validators.Required(),
        validators.Length(min_length=1, max_length=2)
    ])
    submit = fields.SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = fields.StringField('Username*:', validators=[
        validators.Required(),
        validators.AlphaNumeric(),
        validators.Length(min_length=8, max_length=models.User.username.type.length),
        validators.NotContainAny([' ', '_', '&', '<', '>', '/', '\\', "'", '"', ',', '.', '=', '-', '+'])
    ])
    password = fields.PasswordField('Password*:', validators=[
        validators.Required(),
        validators.AlphaNumeric(),
        validators.Length(min_length=8, max_length=models.User.password.type.length),
        validators.NotContainAny([' '], message=u'Field must not contain any spaces'),
        validators.DifferentFrom('username')
    ])
    submit = fields.SubmitField('Sign In')


class CreatePostForm(FlaskForm):
    title = fields.StringField('Title*:', validators=[
        validators.Required(),
        validators.Length(max_length=models.Post.title.type.length)
    ])
    body = fields.TextAreaField('Body*:', validators=[
        validators.Required(),
        validators.Length(max_length=models.Post.body.type.length)
    ])
    submit = fields.SubmitField('Submit')
