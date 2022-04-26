from flask import Flask
from flask import render_template
from dotenv import load_dotenv
import os
from models import db
from middleware import login_manager
from routes.uploadimg import uploadimg
from routes.login import login
from routes.submit import submit
from routes.result import result
from routes.download import download
from routes.logout import logout
app = Flask(__name__)
load_dotenv('.env')
from middleware.auth import *
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost:5433/OCR"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test1234@localhost:5433/OCR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db.init_app(app)
login_manager.init_app(app)
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
