# This file contains a Config class to use for configuring a flask application
import os

class Config(object):

    SECRET_KEY = 'b"z\xbah\x81\xe3\xd7O\xad\xab\xad/9\x84t\n5M8\x05g\xed\x85\xeb\x81\xbeQ\x93\xe7n\xfd\x89_`\x990\xd28\xb9*\x93nT\xed\xdc\xcd\xc5V' # Secret Key for encrypting cookie
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blogsiteDatabase.db'  # database location
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # do not track modifications to database
    SQLALCHEMY_ECHO = True  # log all statements issued - useful for debugging
    WTF_CSRF_ENABLED = False  # disable flask-WTF built-in CSRF form protection
    SESSION_COOKIE_SECURE = True # Sets the cookie with the secure flag so it can only be transmitted across encrypted channels
    SESSION_COOKIE_HTTPONLY = True # Prevents the cookie being accessed through client-side scripts