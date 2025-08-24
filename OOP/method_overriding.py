class parent:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("this is parent class")
class child(parent):
    def __init__(self, child_name):
        self.child_name=child_name
    def hello(self):
        print("this is child class")

child1 = child("razon")
child1.hello()  # parent class have the same method, but here it will work for child class         