from flask import Flask, request, render_template, url_for, send_from_directory, redirect
from store.impl_csv.impl_csv import ImageStore
import random, string
import os


app = Flask(__name__)
UPLOAD_DIRECTORY = "static/img"
image_store = ImageStore("./data/images.csv")

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
 
# all image view 
@app.route('/') 
def index():
  # get all image from store
  images, err = image_store.get_all()
  if err != None:
    return render_template("error.html", ErrorMethod="InternalServerError", ErrorDescription=err)
  # render all image
  return render_template("index.html", images=images)

@app.route('/upload', methods=['POST'])
def upload():
  if 'file' not in request.files:
    return render_template('error.html', ErrorMethod="BadRequest", ErrorDescription="No file selected")
  
  file = request.files['file']
  title = request.form['title']
  filename = randomname(10)+".jpg"
  file.save(os.path.join(UPLOAD_DIRECTORY, filename))
  
  err = image_store.create(filename, title)
  if err != None:
    return render_template("error.html", ErrorMethod="InternalServerError", ErrorDescription=err)
  return redirect(url_for('index'))

@app.route('/image/<file_name>', methods=['GET'])
def send_image(file_name):
  return send_from_directory(UPLOAD_DIRECTORY, file_name)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)