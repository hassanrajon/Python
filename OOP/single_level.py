class user:
    def __init__(self):
         print("parent class")
class student(user):
    def __init__(self):
        super().__init__()
        print("child class")
#! this is single level inheritance
stu = student()     
            