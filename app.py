from flask import Flask
from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv('.env')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
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


@app.route("/login", methods=["GET", "POST"])
def Log_in():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        if username == "admin" and password == "admin":
            return render_template("dashboard.html")
        else:
            flash("Invalid username or password")
            return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
