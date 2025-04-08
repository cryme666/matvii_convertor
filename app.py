from flask import Flask, render_template, request,send_file
from convertor import *
import os
from dotenv import load_dotenv

ALLOWED_EXTENTIONS = ['jpg','csv','jpg','png','xlsx']

UPLOAD_FOLDER = FOLDER

load_dotenv()


app = Flask('Converter')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/',methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/convertation',methods = ['GET', 'POST'])
def convertation():
    file = request.files['file']
    conversion_type = request.form['select']

    file_extention = file.filename.split('.')[1]
    print(file_extention)

    if file_extention not in ALLOWED_EXTENTIONS:
        return 'We can not convert such type of file!'
    
    if conversion_type == 'jpg_to_png' and file_extention != 'jpg':
        return 'Choose jpg file'
    elif conversion_type == 'png_to_jpg' and file_extention != 'png':
        return 'Choose png file'
    # todo add another extensions

    file_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    file.save(file_path)

    if conversion_type == 'jpg_to_png':
        new_file = jpg_to_png(file_path)
    # todo add another extensions


    return send_file(new_file,as_attachment=True)


if __name__ == '__main__':
    app.run(debug = True)