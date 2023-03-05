"""This module takes all routes and adds them to an array of blueprints for use by the 'create_app'
function. The first element of each tuple is the blueprint's 'url_prefix' and the second element is
the route object itself."""
from routes import main

blueprints = [
    ("", main),
]
