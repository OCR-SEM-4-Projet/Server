from flask import Blueprint,render_template,request,flash
from flask_login import login_required
submit = Blueprint(name="submit", import_name=__name__)
from app import db
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
                Results = Result(seat_no=Prn, name=Name, Mcq_marks=Mcq_marks,q2_marks=q2_marks,q3_marks=q3_marks,Tot_des_marks=Tot_des_marks,Tot_marks=Tot_marks,subject=subject_name,college_name=collegename)
                db.session.add(Results)
                db.session.commit()
            flash("Successfully added")
        except Exception as e:
            print(e)
            flash("Error")
        return render_template("dashboard.html")
        
    return render_template('dashboard.html')