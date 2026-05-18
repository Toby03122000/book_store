from user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["password"])
            users.append(item)
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [
            user.username, user.password])
        return None

    # Find a single user by their id
    # def find(self, user_id):
    #     rows = self._connection.execute(
    #         'SELECT * from users WHERE id = %s', [user_id])
    #     row = rows[0]
    #     return User(row["id"], row["username"], row["password"])

    # Delete an user by their id
    # def delete(self, user_id):
    #     self._connection.execute(
    #         'DELETE FROM users WHERE id = %s', [user_id])
    #     return None