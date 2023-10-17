import mysql.connector
import datetime
from env import Env
from logger import Logger

# 初期化段階でDBセッションを作る
class Repository:
    def __init__(self,logger):
        self.logger = logger
        self.e = Env().LoadEnv()
        
        try :
            self.conn = mysql.connector.connect(
            host=self.e.DBhost,
            user=self.e.DBuser,
            passwd=self.e.DBpass,
            db=self.e.DBname,
        )
        except Exception as err:
            self.logger.ERROR(err)
            exit(1)
        self.logger.INFO("DB接続完了")

    def __del__(self):
        self.conn.close()
        self.logger.INFO("DB接続終了")
        
    # ユーザの単一取得
    def GetUser(self,id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            user = cur.fetchone()
            self.logger.DEBUG("ユーザ取得完了")
        return user
    
    # PageSize と PageID を指定して任意の数のユーザを取得
    def GetUsers(self,psize :int,pid :int):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id,name,password,email,created_at FROM users LIMIT %s OFFSET %s", (psize,pid,))
            users = cur.fetchall()
            self.logger.DEBUG("ユーザ取得完了")
        return users

    # ユーザの追加
    def CreateUser(self, name :str , password :str , email :str):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO users (name,password,email,created_at) VALUES (%s,%s,%s,%s)", (name,password,email,datetime.datetime.now(),))
            user = cur.fetchone()
            self.logger.DEBUG("ユーザ追加完了")
        self.conn.commit()
        return user
    
    # 任意のユーザを削除
    def DeleteUser(self, uid:str):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (uid,))
            self.logger.DEBUG("ユーザ削除完了")
        self.conn.commit()
        
    # ユーザの全削除
    def DeleteAllUsers(self):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM users")
            self.logger.DEBUG("ユーザ全削除完了")
        self.conn.commit()