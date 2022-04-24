from flask import Flask
from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv('.env')
from OCRdataExtract import over_all, q2_q3_marks
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost:5433/OCR"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"


class Result(db.Model):
    __tablename__ = "result"
    id = db.Column(db.Integer, primary_key=True)
    seat_no = db.Column(db.String)
    name = db.Column(db.String)
    Mcq_marks = db.Column(db.Integer, nullable=False)
    q2_marks = db.Column(db.Integer, nullable=False)
    q3_marks = db.Column(db.Integer, nullable=False)
    Tot_des_marks = db.Column(db.Integer, nullable=False)
    Tot_marks = db.Column(db.Integer, nullable=False)
    # conform_by = db.Column(db.Integer, db.ForeignKey("admin.id"))

    def __repr__(self) -> str:
        return f"{self.id} - {self.name} - {self.seat_no}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def Log_in():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        if username == "admin" and password == "admin":
            return render_template("dashboard.html")
        else:
            flash("Invalid username or password")
            return render_template("index.html")


@app.route('/uploadimg',methods=['GET','POST'])
def uploadimg():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('OCR/images', file.filename))
        import json
        with open('actual_res.json', encoding='utf-8') as f:
            data = json.load(f)
        data = data['textAnnotations']
        data = over_all(data)
        return render_template('ocrcontain.html',datas = data)
    else:
        return render_template('dashboard.html')

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method =='POST':
        print("--->>  ")
        count = int(request.form["count"])
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
            Results = Result(seat_no=PRN, name=Name, Mcq_marks=Mcq_marks,q2_marks=q2_marks,q3_marks=q3_marks,Tot_des_marks=q2_marks+q3_marks,Tot_marks=q2_marks+q3_marks+Mcq_marks)
            db.session.add(Results)
            db.session.commit()
        return "work"
        
    return "o"

@app.route('/result',methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        seat_no = request.form["seat_no"]
        full_name = request.form["full_name"]
        print(seat_no,full_name)
        data = Result.query.filter_by(seat_no=seat_no,name=full_name).first()
        print(data)
        return "p"
        # return render_template('result.html',data=data)
    else:
        return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)
