from flask import Flask
from internal.handler.handler import ServerHandler
app = Flask(__name__)


def newRoute():
    return app

app.add_url_rule("/health", view_func=ServerHandler.as_view("health"))