class user:
    def __init__(self,username,passw):
        self.username=username
        self.passw=passw
class student(user):
    def __init__(self, username, passw,name,age):
        super().__init__(username, passw)
        self.name=name
        self.age=age    
            
student1 = student("razon_hassan","Razon1234","Razon",24)  
print(student1.username)
