from datetime import datetime
from app import app, db

class Unsubscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    address = db.Column(db.String(32), index=True)
