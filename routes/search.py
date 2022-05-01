from flask import Blueprint, redirect,render_template,request,flash,send_file
from models import db
from models.Marksheet import marksheet
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
            marksheet_search = marksheet.query.filter(marksheet.collegename==collegename,marksheet.branch==branch,marksheet.semester==semester,marksheet.subject==subject,marksheet.isvalid==True).all()
            
            db.session.commit()
            print('--->>>>',marksheet_search)
            if marksheet_search:
                return render_template('dashboard.html',markshit_list=marksheet_search)
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