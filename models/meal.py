from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    date_hour = db.Column(db.DateTime, nullable=False)
    in_diet = db.Column(db.Boolean, nullable=False)
