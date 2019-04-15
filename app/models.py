from datetime import datetime
from app import app, db, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Unsubscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String(32))
    sf_response = db.Column(db.String(32))
    previously = db.Column(db.Boolean)

    def __repr__(self):
        return '<Email {}>'.format(self.email)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
