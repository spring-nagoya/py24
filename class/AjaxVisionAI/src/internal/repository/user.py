from internal.driver.mysql import MySQLConn

class User():
    def __init__(self, dbconn):
        self.dbconn = dbconn

    def get_user(self, user_id):
        self.dbconn.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.fetchone()


    def get_users(self, limit: int = 10, offset: int = 0):
        self.dbconn.execute("SELECT * FROM users LIMIT %s OFFSET %s",(limit, offset))
        return self.fetchone()

    def add_user(self, user):
        pass

    def update_user(self, user):
        pass

    def delete_user(self, user_id):
        pass