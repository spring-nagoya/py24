from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/call_ajax", methods=["GET", "POST"])
def call_ajax():
    if request.method == "POST":
        form_data = request.form.get("fdata")
        data = {"key": form_data}
        return jsonify(data)
    
    # if request.method == "GET":
        # return "GET"
    else:
        return jsonify({"test": "get-test"})


if __name__ == "__main__":
    app.run(debug=True)
