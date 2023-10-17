import os 
class Env:
    def __init__(self):
        # default value
        self.DBhost = "127.0.0.1"
        self.DBport = "3306"
        self.DBuser = "mysql"
        self.DBpass = "mysql"
        self.DBname = "task"
    
    def LoadEnv(self):
        if os.getenv("DB_HOST") != None:
            self.DBhost = os.getenv("DB_HOST")
        if os.getenv("DB_PORT") != None:
            self.DBport = os.getenv("DB_PORT")
        if os.getenv("DB_USER") != None:
            self.DBuser = os.getenv("DB_USER")
        if os.getenv("DB_PASS") != None:
            self.DBpass = os.getenv("DB_PASS")
        if os.getenv("DB_NAME") != None:
            self.DBname = os.getenv("DB_NAME")
        return self