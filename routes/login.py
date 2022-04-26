from flask import Blueprint,render_template,request,flash
from flask_login import login_user
from models.Admin import admin
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
            return render_template("dashboard.html")
        else:
            flash("Invalid username or password")
            return render_template("index.html")