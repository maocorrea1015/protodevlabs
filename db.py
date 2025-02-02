from models import db

def create_db(app):
    with app.app_context():
        db.create_all()
