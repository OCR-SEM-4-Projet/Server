from flask import Blueprint, redirect,render_template,request,flash
from flask_login import login_user
from models import db
from models.Admin import admin
from models.Markshit import markshit
login = Blueprint(name="login", import_name=__name__)
@login.route("", methods=['GET','POST'])
def logins():
    if request.method == "GET":
        print("--->>  ")
        return render_template("index.html")
    elif request.method == "POST":
        print("--->>  ")
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        cheking = admin.query.filter_by(
                username=username, password=password).first()
        if cheking:
            login_user(cheking)
            return redirect('/uploadimg')
        else:
            flash("Invalid username or password")
            return render_template("index.html")