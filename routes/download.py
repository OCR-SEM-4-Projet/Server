from flask import Blueprint,render_template,request,flash,send_file
from app import db
from public.ResultPdf import sendPdf
download = Blueprint(name="download", import_name=__name__)
@download.route('',methods=['POST'])
def downloads():
    if request.method == 'POST':
        try:
            seat_no = request.form["seat_no"]
            # full_name = request.form["full_name"]
            # print(seat_no,full_name)
            data = list(db.session.execute(f"""select "subject","Mcq_marks","q2_marks","q3_marks","Tot_des_marks","Tot_marks" from result where seat_no ='{seat_no}'""").all())
            info = list(db.session.execute(f"""select name, seat_no,college_name from result where seat_no ='{seat_no}'""").first())
            print(info)
            new_data2 = list()
            new_data = list()
            name_list = ["Subject","Mcq Marks","Q2 Marks","Q3 Marks","Total Descriptive Marks","Total Marks"]
            new_data.append(name_list)
            for d in data:
                new_data2.append(list(d))
                new_data.append(list(d))

            print('---------------- >>>>>>>>>>>>> ',new_data)
            path = sendPdf(new_data,info)
            return send_file(path,as_attachment=True)
        except Exception as e:
            print(e)
            flash("Error")
            return render_template('index.html')