from flask import Blueprint, render_template,request,flash, redirect,url_for
import os
from werkzeug.utils import secure_filename



main = Blueprint('main', __name__)


@main.route("/")
def index():
    # return 'Template test'
    return render_template('index.html')



@main.route("/upload_file", methods = ['POST','GET'])
def upload_vlan_data():
    if request.method == 'POST':
        filename = request.form.get('vlan_file')
        dir = './vlan_tmpl/static/files/'
       
        raw_data = dir + filename
        flash('data uploaded successfully')
        return redirect(url_for('main.clean_vlan_data', raw_data = raw_data))
    return render_template('index.html')


@main.route('/clean_data', methods = ['POST','GET'])
def clean_vlan_data():
    if request.method == 'GET':
        raw_data = request.args.get('raw_data')
       
        with open (raw_data) as infile:
            output = infile.read()
    return render_template('index.html', data = output)
    
    # data = request.args.get('data')
    # with open(data) as file:

