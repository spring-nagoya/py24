"""
MIT License

Copyright (c) 2023 spring-nagoya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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