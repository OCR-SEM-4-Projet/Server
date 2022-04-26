from flask_login import UserMixin
from . import db
class admin(db.Model,UserMixin):
    __tablename__ = "adminuser"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String, unique=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"