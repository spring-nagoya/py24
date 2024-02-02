from Flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/call_ajax", methods=["GET","POST"])
def call_ajax():
    if request.method == "POST":
        form = request.form["fdata"]
    if request.method == "GET":
        return "GET"
      
if __name__ == "__main__":
    app.run(debug=True)