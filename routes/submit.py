from flask import Blueprint, redirect,render_template,request,flash, session
from flask_login import login_required

from models.Marksheet import marksheet
submit = Blueprint(name="submit", import_name=__name__)
from models import db
from models.Result import Result
@submit.route("", methods=['GET','POST'])
@login_required
def submits():
    if request.method =='POST':
        try:
            print("--->>  ")
            count = int(request.form["count"])
            subject_name = request.form["subname"]
            collegename = request.form["collegename"]
            semester = request.form["semester"]
            branchname = request.form["branchname"]
            print(count)
            for i in range(1,count):
                Prn = request.form['prn'+str(i)]
                Name = request.form['name'+str(i)]
                try:
                    Mcq_marks = int(request.form['mcq'+str(i)])
                    q2_marks =  int(request.form['q2'+str(i)])
                    q3_marks = int(request.form['q3'+str(i)])
                except Exception as e:
                    Mcq_marks = 0
                    q2_marks = 0
                    q3_marks = 0
                Tot_des_marks=q2_marks+q3_marks
                Tot_marks=q2_marks+q3_marks+Mcq_marks
                print(Prn,Name,Mcq_marks,q2_marks,q3_marks)
                Results = Result(seat_no=Prn, name=Name, Mcq_marks=Mcq_marks,q2_marks=q2_marks,q3_marks=q3_marks,Tot_des_marks=Tot_des_marks,Tot_marks=Tot_marks,marksheet_id=session['marksheet_id'])
                db.session.add(Results)
                db.session.commit()
            marksheet_update = marksheet.query.filter_by(id=session['marksheet_id']).first()
            marksheet_update.semester = semester
            marksheet_update.branch = branchname
            marksheet_update.collegename=collegename
            marksheet_update.subject=subject_name
            marksheet_update.isvalid=True
            db.session.commit()


            flash("Successfully added")
        except Exception as e:
            print(e)
            flash("Error")
        return redirect('/uploadimg')
        
    return redirect('/uploadimg')