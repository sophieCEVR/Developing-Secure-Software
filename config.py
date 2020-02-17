# This file contains a Config class to use for configuring a flask application


class Config(object):
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blogsiteDatabase.db'  # database location
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # do not track modifications to database
    SQLALCHEMY_ECHO = True  # log all statements issued - useful for debugging
    WTF_CSRF_ENABLED = False  # disable flask-WTF built-in CSRF form protection
