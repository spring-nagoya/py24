from repository import Repository
from logger import Logger
class Service:
    def __init__(self,logger):
        self.logger = logger
        self.r = Repository(logger)
        
    # ユーザの追加
    def CreateUser(self, name :str , password :str , email :str):
        user = ""
        try:
            user = self.r.CreateUser(name,password,email)
        except Exception as err:
            return None , err
        return user , None

    # ユーザの単一取得
    def GetUser(self, id):
        user = ""
        try:
            user = self.r.GetUser(id)
        except Exception as err:
           return None , err
        return user , None

    # PageSize と PageID を指定して任意の数のユーザを取得
    def ListUser(self, psize :int,pid :int):
        users = ""
        try:
            users = self.r.GetUsers(psize,pid)
        except Exception as err:
            return None , err
        return users ,None

    # 任意のユーザを削除
    def DeleteUser(self, uid:str) -> Exception:
        user = ""
        try:
            self.r.DeleteUser(uid)
        except Exception as err:
            return err
        return None
            
    # ユーザの全削除
    def DeleteAllUsers(self) -> Exception:
        user = ""
        try:
            self.r.DeleteAllUsers()
        except Exception as err:
            return err
        return None