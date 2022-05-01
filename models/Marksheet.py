from . import db
from .Admin import admin

class marksheet(db.Model):
    __tablename__ = "marksheet"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    semester = db.Column(db.String)
    branch = db.Column(db.String)
    conformbyadmin = db.Column(db.Integer, db.ForeignKey('adminuser.id'))
    collegename = db.Column(db.String)
    subject = db.Column(db.String)
    isvalid = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return f"{self.id} - {self.image_url}"