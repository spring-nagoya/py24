from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/upload/', method = ['GET', 'POST'])
def upload():
  
  if request.method == 'GET':
    return render_template('upload.html')
  
  elif request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join("./static/img", f.filename))
    return redirect(url_for('uploaded_file', filename = f.filename))
  
@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
  return render_template('uploaded_file.html', filename = filename)