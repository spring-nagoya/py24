from repository import Repository

class Service:
    def __init__(self):
        self.r = Repository()
        
    # ユーザの追加
    def CreateUser(self, name :str , password :str , email :str):
        user = ""
        try:
            user = self.r.CreateUser(name,password,email)
        except Exception as e:
            return None , e
        return user , None

    # ユーザの単一取得
    def GetUser(self, id):
        user = ""
        try:
            user = self.r.GetUser(id)
        except Exception as e:
           return None , e
        return user , None

    # PageSize と PageID を指定して任意の数のユーザを取得
    def ListUser(self, psize :int,pid :int):
        users = ""
        try:
            users = self.r.GetUsers(psize,pid)
        except Exception as e:
            return None , e
        return users ,None

    # 任意のユーザの情報を更新
    def UpdateUser(self, uid:str, name: str, password: str ,email :str):
        user = ""
        try:
            user = self.r.UpdateUser(uid,name,password,email)
        except Exception as e:
            print(e)
        return user

    # 任意のユーザを削除
    def DeleteUser(self, uid:str):
        user = ""
        try:
            user = self.r.DeleteUser(uid)
        except Exception as e:
            print(e)
            
    # ユーザの全削除
    def DeleteAllUsers(self):
        user = ""
        try:
            user = self.r.DeleteAllUsers()
        except Exception as e:
            print(e)