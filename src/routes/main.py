"""This module contains the 'main' blueprint which contains the 'home' route to the application."""
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    """The home route to the application."""
    return 'HOME'
