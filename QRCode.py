from ast import dump
import pyqrcode
import cgi
from flask import Flask, render_template, request
import os
app = Flask(__name__, template_folder='template')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    form = cgi.FieldStorage()
    link = str(request.form['link'])
    qr_code = pyqrcode.create(link)
    qr_code.png("static/QRCode.png", scale=6)
    PEOPLE_FOLDER = os.path.join('static')
    app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'QRCode.png')
    return render_template("output.html", user_image = full_filename)
 
if __name__ == '__main__':
    app.run('127.0.0.1', 8085)