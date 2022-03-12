from distutils.command.config import config
from flask import Blueprint, render_template,request,flash, redirect,url_for,session
import os
from werkzeug.utils import secure_filename

from vlan_tmpl.main.utils import allowed_file

UPLOAD_FOLDER = './vlan_tmpl/static/files'







main = Blueprint('main', __name__)


@main.route("/")
def index():
    # return 'Template test'
    return render_template('index.html')



@main.route("/upload_file", methods = ['POST','GET'])
def upload_vlan_data():
    if request.method == 'POST':
#check if the post request has the file path
        if 'file' not in request.files:
            flash('No file path','danger')
            return redirect(request.url)
        
        file = request.files['file']

        #if the user does not submit a file, the browser
        #submits an empty file without a filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER,filename))
            flash('File uploaded successfully','success')
            session['file'] = filename
            
            return render_template('index.html', convert = 'Hello')
    return render_template('index.html')


@main.route('/convert_data', methods = ['POST','GET'])
def convert_vlan_data():
    if request.method == 'GET':
        filename = session.get('file')
        
        with open(f"{UPLOAD_FOLDER}/{filename}") as file:
            output = file.read()
        return render_template('index.html', data = output)
       
    #     with open (raw_data) as infile:
    #         output = infile.read()
    # return render_template('index.html', data = output)
    
    # data = request.args.get('data')
    # with open(data) as file:

