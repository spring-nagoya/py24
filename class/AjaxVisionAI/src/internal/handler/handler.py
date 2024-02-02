from flask.views import View

class ServerHandler(View):
    def dispatch_request(self):
        return "Hello, World!"