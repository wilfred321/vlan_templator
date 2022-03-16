from distutils.command.config import config
from flask import Blueprint, render_template,request,flash, redirect,url_for,session
import os
from werkzeug.utils import secure_filename

from vlan_tmpl.main.utils import allowed_file,edit_filename

import re

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
            session['filename'] = filename
            
            return render_template('index.html', convert = 'Hello')
    return render_template('index.html')


@main.route('/convert_data', methods = ['POST','GET'])
def convert_vlan_data():
    if request.method == 'GET':
        filename = session.get('filename')
        # result_file = filename + ''
        
        raw_data = open(f"{UPLOAD_FOLDER}/{filename}")
        infile = open(f"{UPLOAD_FOLDER}/{edit_filename(filename)}",'w')
        output = []
        counter = 0
        match_dict = []

        
        for i in range(100):
            result = raw_data.readline()
            # stop_going = re.compile(r"VLAN Type")
            pattern = re.compile(r"(?P<vlan_id>\d{1,4})\s+(?P<vlan_name>[\w-]+)\s+")
            matches = pattern.finditer(result)
            for match in matches:
                vlan_name = match['vlan_name']
                vlan_id = match['vlan_id']
              
                #Exclude default vlan 1
                if vlan_id == '1':
                    pass
                else:
                    tmpl = f'{vlan_name}: {vlan_id}\n'
                    infile.write(tmpl)
                    output.append(tmpl)
                    counter += 1
               
        infile.close()
        flash(f'a total of {counter} lines were written to the new file','success')


        return render_template('index.html', data = output)
    return redirect(request.url)










    
       
    #     with open (raw_data) as infile:
    #         output = infile.read()
    # return render_template('index.html', data = output)
    
    # data = request.args.get('data')
    # with open(data) as file:

