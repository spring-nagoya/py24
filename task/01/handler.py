from service import Service
from flask import *


nil = None

class Handler:
    def __init__(self):
        self.s = Service()
    
    # インデックスページ
    def Index(self):
        return render_template("index.html")
    
    # ユーザ追加ページ
    def CreateUserPage(self):
        return render_template("create_user.html")
    
    # ユーザ追加処理
    def CreateUser(self,req):
        user ,err = self.s.CreateUser(req.form['name'],req.form['password'],req.form['email'])
        if err != nil:
            print(err)
            return render_template("create_user.html",msg="ユーザ追加に失敗しました")
        return  render_template("create_user.html",msg="ユーザを追加しました")
    
    def ListUser(self ,req):
        size:int
        id:int 
        try:
            size = int(req.args.get("page_size"))
            id = int(req.args.get("page_id"))
        except Exception as err:
            print(err)
            return render_template("list_user.html",users="" ,msg="不正なパラメータ")        
       
        users ,err = self.s.ListUser(size,(int(id) - 1) * size)
        if err != nil:
            print(err)
            return render_template("list_user.html",users="" ,msg="ユーザ取得に失敗しました")
        return render_template("list_user.html",users=users ,msg="")
    
    def GetUser(self,uid:int):
        user ,err = self.s.GetUser(uid)
        if err != nil:
            print(err)
            return render_template("user.html",user="" ,msg="ユーザ取得に失敗しました")
        return render_template("user.html",user=user ,msg="")
    
    def DeleteUser(self, uid:int):
        if self.s.DeleteUser(uid) != nil:
            return jsonify({"message":"ユーザ削除に失敗しました"}),500
        return jsonify({"message":"ユーザを削除しました"}),200

    def DeleteAllUser(self):
        if self.s.DeleteAllUsers() != nil:
            return jsonify({"message":"ユーザ削除に失敗しました"}),500
        return jsonify({"message":"ユーザを削除しました"}),200
        