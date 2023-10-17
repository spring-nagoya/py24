from flask import Flask, request
from handler import Handler

GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return Handler().Index()

@app.route("/create_user",methods=[GET])
def createuser():
    return Handler().CreateUserPage()

@app.route("/users",methods=[GET,POST,DELETE])
def UsersRouter():
    h = Handler()
    if request.method == GET:
        return h.ListUser(request)
    elif request.method == POST:
        return h.CreateUser(request)
    elif request.method == DELETE:
        return h.DeleteAllUser()
    else:
        return "不正なメソッドです"

@app.route("/users/<uid>",methods=[GET,DELETE])
def User(uid):
    if request.method == GET:
        return Handler().GetUser(uid)
    elif request.method == DELETE:
        return Handler().DeleteUser(uid)
    else:
        return "不正なメソッドです"

if __name__ == "__main__":
    app.run(debug=True)