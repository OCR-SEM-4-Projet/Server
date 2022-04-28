from flask import Blueprint,render_template,request,flash,send_file
from app import db
from public.ResultPdf import sendPdf
download = Blueprint(name="download", import_name=__name__)
@download.route('',methods=['POST'])
def downloads():
    if request.method == 'POST':
        try:
            seat_nos = request.form["seat_no"]
            semester = request.form["semester"]
            data = db.session.execute(f"""select  markshit.subject, "Mcq_marks","q2_marks","q3_marks","Tot_des_marks","Tot_marks" as ms from result INNER JOIN markshit ON result.markshit_id = markshit.id AND result.seat_no = '{seat_nos}' AND markshit.semester = '{semester}' AND markshit.isvalid = True""").fetchall()
            
            info_data = db.session.execute(f"select result.name,markshit.branch, markshit.collegename,markshit.semester from markshit INNER JOIN result ON markshit.id = result.markshit_id AND result.seat_no = '{seat_nos}' AND markshit.semester = '{semester}' AND markshit.isvalid = True ORDER BY markshit.id ASC LIMIT 1;").fetchall()
            db.session.commit()
            print(info_data)
            print(data)


            # data = list(db.session.query(Result.subject,Result.Mcq_marks,Result.q3_marks,Result.q3_marks,Result.Tot_des_marks,Result.Tot_marks).filter().all())
            # info = list(db.session.execute(f"""select name, seat_no,college_name from result where seat_no ='{seat_nos}'""").first())
            # print(info)
            new_data2 = list()
            new_data = list()
            name_list = ["Subject","Mcq Marks","Q2 Marks","Q3 Marks","Total Descriptive Marks","Total Marks"]
            new_data.append(name_list)
            for d in data:
                new_data2.append(list(d))
                new_data.append(list(d))
            print(new_data2)
            path = sendPdf(new_data,info_data,seat_nos)
            return send_file(path,as_attachment=True)
        except Exception as e:
            print(e)
            flash("Error")
            return render_template('index.html')