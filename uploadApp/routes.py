
from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField
from werkzeug import secure_filename
import io
import base64

from uploadApp import app

@app.route("/")
@app.route("/home/")
def index():
    text = "Welcome to student file upload"
    return text

@app.route('/upload/')
def upload_file():
    return render_template('uploadfile.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      name = f.filename

      img1 = f.read()
      img2 = base64.b64encode(img1)
      img3 = img2.decode("ascii", "ignore")

      return render_template("index.html", name=name, image=img3)
