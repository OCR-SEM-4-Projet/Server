from hashlib import sha512
import uuid
from flask import Blueprint, redirect,render_template,request, session
from flask_login import current_user, login_required
import os
from public.OCRdataExtract import over_all
from models import db
from models.Marksheet import marksheet
uploadimg = Blueprint(name="uploadimg", import_name=__name__)
@uploadimg.route("", methods=['GET','POST'])
@login_required
def uploadimgs():
    if request.method == 'POST':
        try:
            file = request.files['file']
            file_extension = os.path.splitext(file.filename)[1]
            file_name = str(file.filename)+uuid.uuid4().hex
            file_name = file_name.encode('utf-8')
            hash_filename = sha512(file_name).hexdigest()+str(file_extension)
            file.save(os.path.join('static/OCR/images', hash_filename))
            current_admin = current_user.id
            marksheets = marksheet(image_url=hash_filename,conformbyadmin=current_admin)
            db.session.add(marksheets)
            db.session.commit()
            marksheet_id = marksheets.id
            session['marksheet_id'] = marksheet_id
            print(marksheet_id,session['marksheet_id'])
            import json
            with open('public/actual_res.json', encoding='utf-8') as f:
                data = json.load(f)
            data = data['textAnnotations']
            data = over_all(data)
            return render_template('ocrcontain.html',datas = data)
        except Exception as e:
            print(e)
            return redirect('/uploadimg')
    else:
        marksheet_list = marksheet.query.filter(marksheet.isvalid==True).limit(5).all()
        db.session.commit()
        print(marksheet_list)
        return render_template('dashboard.html',markshit_list=marksheet_list)