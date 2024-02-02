from flask import Flask
from internal.handler.handler import HealthHandler , IndexHandler
app = Flask(__name__,template_folder='../../templates')


def newRoute():
    return app

app.add_url_rule("/",view_func=IndexHandler.as_view("index"))
app.add_url_rule("/health", view_func=HealthHandler.as_view("health"))