"""This module contains the DefaultConfig class which houses the application's configurations when
running as a default application."""


class DefaultConfig:
    """The DefaultConfig object initializes a given flask app's configurations."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///default'
