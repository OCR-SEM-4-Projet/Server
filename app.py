import datetime
from flask import Flask, redirect, send_file
from flask import render_template, request, flash
from flask_login import LoginManager, login_manager, logout_user, AnonymousUserMixin, login_user
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from ResultPdf import sendPdf
import os
app = Flask(__name__)
load_dotenv('.env')
from OCRdataExtract import over_all
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost:5433/OCR"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test1234@localhost:5433/OCR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
from models import db
db.init_app(app)
from models.Result import Result
from models.Admin import admin
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'
@login_manager.user_loader
def load_user(user_id):
    return admin.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        cheking = admin.query.filter_by(
                username=username, password=password).first()
        if cheking:
            login_user(cheking)
            return render_template("dashboard.html")
        else:
            flash("Invalid username or password")
            return render_template("index.html")


@app.route('/uploadimg',methods=['GET','POST'])
@login_required
def uploadimg():
    if request.method == 'POST':
        try:
            file = request.files['file']
            file.save(os.path.join('OCR/images', file.filename))
            import json
            with open('actual_res.json', encoding='utf-8') as f:
                data = json.load(f)
            data = data['textAnnotations']
            data = over_all(data)
            return render_template('ocrcontain.html',datas = data)
        except Exception as e:
            print(e)
            return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')

@app.route("/submit", methods = ['GET', 'POST'])
@login_required
def submit():
    if request.method =='POST':
        try:
            print("--->>  ")
            count = int(request.form["count"])
            subject_name = request.form["subname"]
            collegename = request.form["collegename"]
            print(count)
            for i in range(1,count):
                PRN = request.form['prn'+str(i)]
                Name = request.form['name'+str(i)]
                try:
                    Mcq_marks = int(request.form['mcq'+str(i)])
                    q2_marks =  int(request.form['q2'+str(i)])
                    q3_marks = int(request.form['q3'+str(i)])
                except Exception as e:
                    Mcq_marks = 0
                    q2_marks = 0
                    q3_marks = 0
                print(PRN,Name,Mcq_marks,q2_marks,q3_marks)
                Results = Result(seat_no=PRN, name=Name, Mcq_marks=Mcq_marks,q2_marks=q2_marks,q3_marks=q3_marks,Tot_des_marks=q2_marks+q3_marks,Tot_marks=q2_marks+q3_marks+Mcq_marks,subject=subject_name,college_name=collegename)
                db.session.add(Results)
                db.session.commit()
            flash("Successfully added")
        except Exception as e:
            print(e)
            flash("Error")
        return render_template("dashboard.html")
        
    return render_template('dashboard.html')

@app.route('/result',methods=['GET', 'POST'])
def result():
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

@app.route('/download',methods=['POST'])
def download():
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

        # return render_template('result.html',data=data)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Succesfully')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
