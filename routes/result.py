from flask import Blueprint,render_template,request,flash
from app import db
from models.Result import Result
import datetime
from public.ResultPdf import sendPdf
result = Blueprint(name="result", import_name=__name__)
@result.route("", methods=['GET','POST'])
def results():
    if request.method == 'POST':
        try:
            seat_nos = request.form["seat_no"]
            # full_name = request.form["full_name"]
            # print(seat_no,full_name)
            current_date = datetime.datetime.now()
            six_month_before = current_date - datetime.timedelta(days=180)
            six_month_before=six_month_before.strftime("%Y-%m-%d")
            current_date=current_date.strftime("%Y-%m-%d")
            print(six_month_before,current_date)
            data = list(db.session.query(Result.subject,Result.Mcq_marks,Result.q3_marks,Result.q3_marks,Result.Tot_des_marks,Result.Tot_marks).filter(Result.seat_no==seat_nos and Result.date.between(six_month_before,current_date)).all())
            info = list(db.session.execute(f"""select name, seat_no,college_name from result where seat_no ='{seat_nos}'""").first())
            print(info)
            new_data2 = list()
            new_data = list()
            name_list = ["Subject","Mcq Marks","Q2 Marks","Q3 Marks","Total Descriptive Marks","Total Marks"]
            new_data.append(name_list)
            for d in data:
                new_data2.append(list(d))
                new_data.append(list(d))

            print('---------------- >>>>>>>>>>>>> ',new_data)
            sendPdf(new_data,info)
            return render_template('result.html',datas=new_data2,info=info)
        except Exception as e:
            print(e)
            flash("Error")
            return render_template('index.html')
        # return render_template('result.html',data=data)
    else:
        return render_template('index.html')