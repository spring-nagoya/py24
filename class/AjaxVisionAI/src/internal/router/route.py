from flask import Flask
from internal.handler.handler import HealthHandler, IndexHandler, AjaxHandler
from internal.repository.user import User

# Constants
GET= "GET"
POST= "POST"
PUT= "PUT"
DELETE= "DELETE"


class Route:
    def __init__(self,dbconn):
        if  dbconn == None:
            raise Exception("Database connection is not defined")
                                
        self.app = Flask(__name__,template_folder='../../templates', static_folder='../../static')

        user_model = User(dbconn=dbconn)
        # ajaxHandler = AjaxHandler(dbconn=dbconn)
        
        self.add_url_rule("/",view_func=IndexHandler("index",user_model=user_model))
        # self.add_api("/health",HealthHandler.as_view("health"))
        # self.add_api("/call_ajax",ajaxHandler.as_view("call-ajax"))

    def New(self):
        return self.app
    
    def add_api(self,path,handler):
        self.app.add_url_rule(path,view_func=handler)