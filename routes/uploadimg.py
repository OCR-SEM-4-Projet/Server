from hashlib import sha512
import uuid
from flask import Blueprint, redirect,render_template,request, session
from flask_login import current_user, login_required
import os
from public.OCRdataExtract import over_all
from models import db
from models.Markshit import markshit
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
            markshits = markshit(image_url=hash_filename,conformbyadmin=current_admin)
            db.session.add(markshits)
            db.session.commit()
            markshit_id = markshits.id
            session['markshit_id'] = markshit_id
            print(markshit_id,session['markshit_id'])
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
        markshit_list = markshit.query.filter(markshit.isvalid==True).limit(5).all()
        db.session.commit()
        print(markshit_list)
        return render_template('dashboard.html',markshit_list=markshit_list)