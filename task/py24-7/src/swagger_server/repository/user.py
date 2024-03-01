class UserRepo:
    def __init__(self, connection):
        self.connection = connection
        
    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return result

    def get_search_user(self,name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name like '%"+name+"%'")
        result = cursor.fetchall()
        return result
        
    def get_user(self,id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        result = cursor.fetchall()
        return result

    def create_user(self,id, name, age):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (id,name, age) VALUES (%s,%s, %s)", (id,name, age))
        self.connection.commit()

        return self.get_user(id)
    
    def delete_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        self.connection.commit()
    
    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users")
        self.connection.commit()