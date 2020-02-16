from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config  # import the Config class for app configuration

app = Flask(__name__)  # create flask application object
app.config.from_object(Config)  # configure the app using a Config object
db = SQLAlchemy(app)  # create the database object for the application

from . import routes, models, forms  # use the routes, models, and forms of the current package for the app
