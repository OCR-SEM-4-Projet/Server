from flask import Blueprint,render_template,request,flash
from app import db
from models.Result import Result
import datetime
from public.ResultPdf import sendPdf
markshit = Blueprint(name="markshit", import_name=__name__)
@markshit.route("", methods=['GET','POST'])
def markshits():
    return "hi"
