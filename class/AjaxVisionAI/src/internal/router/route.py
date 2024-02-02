from flask import Flask

app = Flask(__name__)
    
def initRoute():
    return app

@app.route("/health")
def health():
    return "OK"