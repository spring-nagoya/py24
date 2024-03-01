import mysql.connector

class MySQLConn:
    def __init__(self, host,port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        
    def connect(self):
        self.conn = mysql.connector.connect(host=self.host,port=self.port,user=self.user, passwd=self.passwd, db=self.db)
    
    def close(self):
        self.conn.close()
        
    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def fetch_all(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result