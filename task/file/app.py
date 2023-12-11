from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import os

app = Flask(__name__)


UPLOAD_FOLDER = "static/img"

def get_image_list():
        image_dir = "static/img"
        images = os.listdir(image_dir)
        return images
    
    
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        
        return render_template("file.html" ,)

    elif request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        return redirect(url_for("uploaded_file", file_name=file.filename))



@app.route("/uploaded_file/<string:file_name>")
def uploaded_file(file_name):
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    return render_template("uploaded_file.html", filename=file_path)


@app.route("/static/img/<string:file_name>")
def send_img(file_name):
    return send_from_directory(UPLOAD_FOLDER, file_name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


