from flask import Blueprint,render_template
index = Blueprint(name="index", import_name=__name__)
@index.route('',methods=['GET'])
def indexs():
    return render_template('index.html')