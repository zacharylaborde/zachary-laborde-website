"""This module acts as the entry point to the application. The flask app-factory method is imported
with the database, the application's context is set, the database is initialized and committed, and
then app starts.
"""
from app import create_app, db

app = create_app()
app.app_context().push()
db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run()
