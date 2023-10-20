from service import Service
from flask import *
from logger import Logger

nil = None

class Handler:
    def __init__(self,logger):
        self.logger = logger
        self.s = Service(logger)
    
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
            self.logger.ERROR(err)
            return render_template("create_user.html",msg="ユーザ追加に失敗しました")
        return  render_template("create_user.html",msg="ユーザを追加しました")
    
    # ユーザ一覧ページ
    def ListUser(self ,req):
        size ,err = Atoi(req.args.get("size"))
        if err != nil:
            self.logger.ERROR(err)
            return render_template("list_user.html",users="" ,msg="不正なリクエスト")
        
        pid ,err = Atoi(req.args.get("id"))
        if err != nil:
            self.logger.ERROR(err)
            return render_template("list_user.html",users="" ,msg="不正なリクエスト")
       
        users ,err = self.s.ListUser(size,(pid - 1) * size)
        if err != nil:
            self.logger.ERROR(err)
            return render_template("list_user.html",users="" ,msg="ユーザ取得に失敗しました")
        return render_template("list_user.html",users=users ,msg="")
    
    def GetUser(self,uid:int):
        user ,err = self.s.GetUser(uid)
        if err != nil:
            self.logger.ERROR(err)
            return render_template("user.html",user="" ,msg="ユーザ取得に失敗しました")
        return render_template("user.html",user=user ,msg="")
    
    def DeleteUser(self, uid:int):
        err = self.s.DeleteUser(uid)
        if err != nil:
            self.logger.ERROR(err)
            return jsonify({"message":"ユーザ削除に失敗しました"}),500
        return jsonify({"message":"ユーザを削除しました"}),200

    def DeleteAllUser(self):
        err = self.s.DeleteAllUsers()
        if  err != nil:
            self.logger.ERROR(err)
            return jsonify({"message":"ユーザ削除に失敗しました"}),500
        return jsonify({"message":"ユーザを削除しました"}),200
    
    

def Atoi(s :str) -> (int,Exception):
    try:
        return int(s),nil
    except ValueError as err:
        return 0,err
    except TypeError as err:
        return 0,err