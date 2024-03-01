class UserRepo:
    def __init__(self, connection):
        self.connection = connection
        
    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return result

    def create_user(self, username, age):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (username, age) VALUES (%s, %s)", (username, age))
        self.connection.commit()
    
    def delete_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        self.connection.commit()
    
    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users")
        self.connection.commit()