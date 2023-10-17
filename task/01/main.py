from flask import Flask, request
from handler import Handler
from logger import *

# constant value 
GET = "GET"
POST = "POST"
DELETE = "DELETE"
ERROR_INVALID_METHOD = "不正なメソッドです"
# 
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
l = Logger("./log/log.txt",0)
@app.route("/")
def index():
    return Handler(l).Index()

@app.route("/create_user",methods=[GET])
def createuser():
    return Handler(l).CreateUserPage()

@app.route("/users",methods=[GET,POST,DELETE])
def UsersRouter():
    h = Handler(l)
    if request.method == GET:
        return h.ListUser(request)
    elif request.method == POST:
        return h.CreateUser(request)
    elif request.method == DELETE:
        return h.DeleteAllUser()
    else:
        return ERROR_INVALID_METHOD

@app.route("/users/<uid>",methods=[GET,DELETE])
def User(uid):
    h = Handler(l)
    if request.method == GET:
        return h.GetUser(uid)
    elif request.method == DELETE:
        return h.DeleteUser(uid)
    else:
        return ERROR_INVALID_METHOD

if __name__ == "__main__":
    app.run(debug=True)
    del l