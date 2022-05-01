from flask import Blueprint, redirect,render_template,request,flash, session
from flask_login import login_required

from models.Marksheet import marksheet
view = Blueprint(name="view", import_name=__name__)
from models import db
from models.Result import Result
@view.route("<int:id>", methods=['GET','POST'])
@login_required
def views(id):
    if request.method =='GET':
        print("--->>  ")
        marksheet_data = marksheet.query.filter_by(id=id).first()
        results = Result.query.filter_by(marksheet_id=int(id)).all()
        db.session.commit()
        print(results)
        return render_template("viewcontaint.html",datas=results,markshit_data=marksheet_data,id=id)
    elif request.method =='POST':
        count = int(request.form["count"])
        results = Result.query.filter_by(marksheet_id=int(id)).first()
        db.session.commit()
        curr_id = results.id
        print(curr_id)
        print(count)
        for i in range(1,count):
            try:
                Prn = request.form['prn'+str(curr_id)]
                Name = request.form['name'+str(curr_id)]
                Mcq_marks = int(request.form['mcq'+str(curr_id)])
                q2_marks =  int(request.form['q2'+str(curr_id)])
                q3_marks = int(request.form['q3'+str(curr_id)])
            except Exception as e:
                Mcq_marks = 0
                q2_marks = 0
                q3_marks = 0
            try:
                Tot_des_marks=q2_marks+q3_marks
                Tot_marks=q2_marks+q3_marks+Mcq_marks
                print(Prn,Name,Mcq_marks,q2_marks,q3_marks)
                res_update = Result.query.filter_by(id=curr_id).first()
                res_update.seat_no=Prn
                res_update.name=Name
                res_update.Mcq_marks=Mcq_marks
                res_update.q2_marks=q2_marks
                res_update.q3_marks=q3_marks
                res_update.Tot_des_marks=Tot_des_marks
                res_update.Tot_marks=Tot_marks
                db.session.commit()
                curr_id += 1
            except Exception as e:
                print(e)
                flash("Error")
                break
            # Results = Result(seat_no=Prn, name=Name, Mcq_marks=Mcq_marks,q2_marks=q2_marks,q3_marks=q3_marks,Tot_des_marks=Tot_des_marks,Tot_marks=Tot_marks,markshit_id=session['markshit_id'])
            # db.session.add(Results)
            # db.session.commit()
        print("--->>  ")
        return redirect('/uploadimg')