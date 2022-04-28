from dotenv import load_dotenv
import os
from models import db
from middleware import login_manager
from routes.index import index
from routes.uploadimg import uploadimg
from routes.login import login
from routes.submit import submit
from routes.result import result
from routes.download import download
from routes.logout import logout
from routes.view import view
from routes.search import search
from middleware.auth import *
def create_app(app):
    load_dotenv('.env')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost:5432/OCR"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test1234@localhost:5433/OCR"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(index,url_prefix='/')
    app.register_blueprint(uploadimg,url_prefix='/uploadimg')
    app.register_blueprint(login,url_prefix='/login')
    app.register_blueprint(submit,url_prefix='/submit')
    app.register_blueprint(result,url_prefix='/result')
    app.register_blueprint(download,url_prefix='/download')
    app.register_blueprint(logout,url_prefix='/logout')
    app.register_blueprint(view,url_prefix='/view')
    app.register_blueprint(search,url_prefix='/search')
    return app