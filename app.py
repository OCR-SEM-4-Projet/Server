from flask import Flask
from flask import render_template
from flask_login import LoginManager, login_manager, AnonymousUserMixin
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost:5433/OCR"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test1234@localhost:5433/OCR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
from models import db
db.init_app(app)
from models.Admin import admin
from routes.uploadimg import uploadimg
from routes.login import login
from routes.submit import submit
from routes.result import result
from routes.download import download
from routes.logout import logout
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.logins'
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'
@login_manager.user_loader
def load_user(user_id):
    return admin.query.get(int(user_id))
app.register_blueprint(uploadimg,url_prefix='/uploadimg')
app.register_blueprint(login,url_prefix='/login')
app.register_blueprint(submit,url_prefix='/submit')
app.register_blueprint(result,url_prefix='/result')
app.register_blueprint(download,url_prefix='/download')
app.register_blueprint(logout,url_prefix='/logout')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
