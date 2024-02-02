from flask.views import View
from flask import request, render_template

class HealthHandler(View):
    def dispatch_request(self):
        return "Hello, World!"
    
    
class IndexHandler(View):
    def dispatch_request(self):
        return render_template("index.html")
    
class AjaxHandler(View):
    def dispatch_request(self):
        return "ajax"