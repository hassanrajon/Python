class MySQLDatabase:
    def save_data(self, data):
        print(f"Saving {data} to MySQL database")


class UserService:
    def __init__(self):
        self.db = MySQLDatabase()   #  Direct dependency on MySQL

    def save_user(self, user):
        self.db.save_data(user)
service = UserService()
service.save_user("Razon")
"""
--> UserService is tightly coupled with MySQLDatabase.
--> If tomorrow you switch to MongoDB, you must change UserService code.
 This violates Dependency inversion.
"""