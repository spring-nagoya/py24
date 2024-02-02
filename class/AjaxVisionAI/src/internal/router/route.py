from flask import Flask
from internal.handler.handler import HealthHandler, IndexHandler, AjaxHandler

# Constants
GET= "GET"
POST= "POST"
PUT= "PUT"
DELETE= "DELETE"


class Route:
    def __init__(self):
        self.app = Flask(__name__,template_folder='../../templates')
        
        self.add_api("/",IndexHandler.as_view("index"))
        self.add_api("/health",HealthHandler.as_view("health"))
        self.add_api("/call-ajax",AjaxHandler.as_view("ajax"))

    def New(self):
        return self.app
    
    def add_api(self,path,handler):
        self.app.add_url_rule(path,view_func=handler)