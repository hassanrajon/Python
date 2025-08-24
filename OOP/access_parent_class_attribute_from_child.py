class user:
    def __init__(self,username,passw):
        self.username=username
        self.passw=passw
class student(user):
    def __init__(self, username, passw,name,age):
        super().__init__(username, passw)
        self.name=name
        self.age=age    
    def info(self):
        print(self.username,self.passw) # here we are accessing parent class's attribute from child class        
student1 = student("razon_hassan","Razon1234","Razon",24)  
print(student1.username)
student1.info()
