# This file contains a Config class to use for configuring a flask application
import os


class Config(object):
    SECRET_KEY = '\xdf\xa2\t`9"\x86\xf3y\x93\xc7,\xd3\xe4\x7f(\x88j%\xd5;\xda\xfcD\xaby\x12\x16\xea7\'\r\xa8\x9b\x95\x8d\xc6\xc7\xb1\x07\n\x04\xcf8-\x06r\xafKi'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blogsiteDatabase.db'  # database location
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # do not track modifications to database
    SQLALCHEMY_ECHO = True  # log all statements issued - useful for debugging
    WTF_CSRF_ENABLED = False  # disable flask-WTF built-in CSRF form protection
    SESSION_COOKIE_SECURE = True # Browser can only send cookies to the server over an encrypted connection
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = 'justJackverify@gmail.com' # os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = 'notsecure'  # os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'justJackverify@gmail.com'
    SESSION_COOKIE_HTTPONLY = True # Prevents cookie being sent over HTTP, only HTTPS

