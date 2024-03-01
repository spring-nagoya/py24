import mysql.connector

class MySQLConnection:
    def __init__(self,host,port,name,user,password):
        self.host = host
        self.port = port
        self.database = name
        self.user = user
        self.password = password

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )
        return self.connection
    
    def close(self):
        self.connection.close()