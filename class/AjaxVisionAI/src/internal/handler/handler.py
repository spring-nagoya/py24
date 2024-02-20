from flask.views import MethodView
from flask import request, render_template, jsonify

class HealthHandler(MethodView):
    def get(self):
        return "ok"
    
    
class IndexHandler(MethodView):    
    def get(self):
        return render_template("index.html")
    
class AjaxHandler(MethodView):    
    def post(self):
        
        reqBody = request.form.get("fdata")
        print(reqBody)
        
        resp = {"key":reqBody}
        
        return jsonify(resp)
    
    def get(self):
        return jsonify({"test":"get"})