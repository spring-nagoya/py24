from Flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/call_ajax", methods=["POST"])
def call_ajax():
    data = request.json
    print(data)
    return json.dumps(data)