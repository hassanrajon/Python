from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save_data(self, data):
        pass


class MySQLDatabase(Database):
    def save_data(self, data):
        print(f"Saving {data} to MySQL database")


class MongoDBDatabase(Database):
    def save_data(self, data):
        print(f"Saving {data} to MongoDB database")


class UserService:
    def __init__(self, db: Database):   #depends on abstraction
        self.db = db
    def save_user(self, user):
        self.db.save_data(user)
        
mysql_db = MySQLDatabase()
mongo_db = MongoDBDatabase()

service1 = UserService(mysql_db)
service1.save_user("Razon")  #Works with MySQL

service2 = UserService(mongo_db)
service2.save_user("Hassan") #Works with MongoDB
