from flask.views import MethodView
from flask import request, render_template, jsonify
from internal.repository.user import User

class HealthHandler(MethodView):
    def __init__(self,dbconn):
        if dbconn is None:
            raise Exception("dbconn is None")
        self.user_repo = User(dbconn)
    
    def get(self):
        return "ok"
    
    
class IndexHandler(MethodView):
    init_every_request = False

    def __init__(self,user: User = None):
        if user is None:
            raise Exception("dbconn is None")
        self.user_repo = user
        
    def get(self):
        # users = self.user_repo.get_users()
        # print(users)
        return render_template("index.html")
    
class AjaxHandler(MethodView):
    def __init__(self,dbconn):
        self.user_repo = User(dbconn)
        
    def post(self):
        reqBody = request.get_json(force=True)
        
        print(reqBody)
        
        return jsonify(reqBody)
    
    def get(self):
        return jsonify({"test":"get"})