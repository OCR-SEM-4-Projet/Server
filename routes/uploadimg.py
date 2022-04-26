from flask import Blueprint,render_template,request
from flask_login import login_required
import os
from public.OCRdataExtract import over_all
uploadimg = Blueprint(name="uploadimg", import_name=__name__)
@uploadimg.route("", methods=['GET','POST'])
@login_required
def uploadimgs():
    if request.method == 'POST':
        try:
            file = request.files['file']
            file.save(os.path.join('OCR/images', file.filename))
            import json
            with open('public/actual_res.json', encoding='utf-8') as f:
                data = json.load(f)
            data = data['textAnnotations']
            data = over_all(data)
            return render_template('ocrcontain.html',datas = data)
        except Exception as e:
            print(e)
            return render_template('dashboard.html')
    else:
        print("error")
        return render_template('dashboard.html')