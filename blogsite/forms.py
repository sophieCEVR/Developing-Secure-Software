# File containing forms for blogsite

from . import models  # import models for validation

from flask_wtf import FlaskForm
from wtforms import validators, fields


class CreateAccountForm(FlaskForm):
    username = fields.StringField('Username*:', validators=[
        validators.InputRequired(),
        validators.Length(min=8, max=models.User.username.type.length)
        #validators.Regexp(r'^\w*[a-zA-Z_]+\w*$', message='Must contain at least 1 alphabetic character and cannot contain special characters')
    ])
    password = fields.PasswordField('Password*:', validators=[
        validators.InputRequired(),
        validators.Length(min=8, max=models.User.password.type.length)
    ])
    passwordConfirm = fields.PasswordField('Confirm Password*:', validators=[
        validators.InputRequired(),
        validators.EqualTo('password')
    ])
    submit = fields.SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = fields.StringField('Username*:', validators=[
        validators.InputRequired(),
        validators.Length(min=8, max=models.User.username.type.length)
        #validators.Regexp(r'^\w*[a-zA-Z_]+\w*$', message='Must contain at least 1 alphabetic character and cannot contain special characters')
    ])
    password = fields.PasswordField('Password*:', validators=[
        validators.InputRequired(),
        validators.Length(min=8, max=models.User.password.type.length)
    ])
    submit = fields.SubmitField('Sign In')


class CreatePostForm(FlaskForm):
    title = fields.StringField('Title*:', validators=[
        validators.InputRequired(),
        validators.length(max=models.Post.title.type.length)
    ])
    body = fields.TextAreaField('Body*:', validators=[
        validators.InputRequired(),
        validators.Length(max=models.Post.body.type.length)
    ])
    submit = fields.SubmitField('Submit')
