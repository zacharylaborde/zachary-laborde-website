"""The purpose of this module is to supply the 'create_app' factory method. The module imports
modules from across the app such as database models and routes and allows them to be accessed simply
through the 'create_app' factory method."""
from flask import Flask

from .configs import DefaultConfig
from .extensions import db
from .blueprints import blueprints


def create_app(config=DefaultConfig):
    """This method is the 'create_app' factory method. It's used to initialize a Flask application
    by first creating the app and then initializing each of the applications extensions using the
    given application configurations. Finally, it registers all blueprints imported into the app's
    blueprints module."""
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    [app.register_blueprint(bp, url_prefix=prefix) for prefix, bp in blueprints]

    return app
