from database import db
from sqlalchemy.sql import func


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)
    date_hour = db.Column(db.DateTime, nullable=True, default=func.now())
    in_diet = db.Column(db.Boolean, nullable=False)
