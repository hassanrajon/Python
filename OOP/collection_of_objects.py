class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(self.name,self.age)     
c1=Customer("razon",25)
c2=Customer("Adnan",24)
c3=Customer("Nayeem",20)   
l = [c1,c2,c3]
for x in l:
    x.intro()     
         