from flask import Blueprint, redirect,render_template,request,flash,send_file
from app import db
from models.Markshit import markshit
from public.ResultPdf import sendPdf
search = Blueprint(name="search", import_name=__name__)
@search.route('',methods=['GET','POST'])
def searchs():
    if request.method == 'POST':
        collegename = request.form["collegename"]
        branch = request.form["branch"]
        semester = request.form["semester"]
        subject = request.form["subject"]
        print(collegename,branch,semester,subject)
        try:
            markshit_search = markshit.query.filter(markshit.collegename==collegename,markshit.branch==branch,markshit.semester==semester,markshit.subject==subject).all()
            
            db.session.commit()
            print('--->>>>',markshit_search)
            if markshit_search:
                return render_template('dashboard.html',markshit_list=markshit_search)
            else:
                flash("No data found")
                return redirect('/uploadimg')
        except Exception as e:
            print(e)
            flash("Error")
            return redirect('/uploadimg')
    else:
        print("--->>  ")
        return redirect('/uploadimg')