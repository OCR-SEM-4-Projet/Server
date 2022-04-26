from flask import Blueprint,render_template,flash
from flask_login import login_required,logout_user
logout = Blueprint(name="logout", import_name=__name__)
@logout.route('')
@login_required
def logouts():
    logout_user()
    flash('Logout Succesfully')
    return render_template('index.html')