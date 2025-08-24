class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(Custome):
    if(Custome.gender=="Male"):
        print("Hello",Custome.name,"sir")
    else:
        print("Hello",Custome.name,"mam")
    cust2=Customer("New customer is createed","Female")
    return cust2    
cust1 = Customer("Razon","Male")
cust2=greet(cust1)
print(cust2.name)
                 