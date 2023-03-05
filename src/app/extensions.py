"""The purpose of this module is to import and initialize each of the flask extensions that will be
utilized in the 'create_app' factory method."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
