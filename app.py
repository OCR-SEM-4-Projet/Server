from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test1234@localhost:5433/OCR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"


class Result(db.Model):
    __tablename__ = "result"
    id = db.Column(db.Integer, primary_key=True)
    seat_no = db.Column(db.String)
    name = db.Column(db.String)
    Mcq_marks = db.Column(db.Integer, nullable=False)
    q2_marks = db.Column(db.Integer, nullable=False)
    q3_marks = db.Column(db.Integer, nullable=False)
    Tot_des_marks = db.Column(db.Integer, nullable=False)
    Tot_marks = db.Column(db.Integer, nullable=False)
    conform_by = db.Column(db.Integer, db.ForeignKey("admin.id"))

    def __repr__(self) -> str:
        return f"{self.id} - {self.name} - {self.seat_no}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login")
def Log_in():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
