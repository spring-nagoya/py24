from flask.views import MethodView
from flask import request, render_template

class HealthHandler(MethodView):
    def get(self):
        return "ok"
    
    
class IndexHandler(MethodView):    
    def get(self):
        return render_template("index.html")
    
class AjaxHandler(MethodView):    
    def get(self):
        return "ajax get"
    
    def post(self):
        # get form data from request
        form_data = request.form.get
        return "ajax post"