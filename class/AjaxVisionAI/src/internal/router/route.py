from flask import Flask
from internal.handler.handler import HealthHandler, IndexHandler, AjaxHandler

# Constants
GET= "GET"
POST= "POST"
PUT= "PUT"
DELETE= "DELETE"

app = Flask(__name__,template_folder='../../templates')


def newRoute():
    return app

app.add_url_rule("/",view_func=IndexHandler.as_view("index"),methods=[GET])
app.add_url_rule("/health", view_func=HealthHandler.as_view("health"),methods=[GET])
app.add_url_rule("/call-ajax", view_func=AjaxHandler.as_view("ajax"),methods=[GET,POST])