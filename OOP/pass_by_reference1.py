class Customer:
    def __init__(self,name):
        self.name=name
def greet(cust):
    cust.name="Razon" # it was passed by reference,so change in here will change in original object
    print(cust.name) 
cust1=Customer("hello")
greet(cust1) #pass by reference
print(cust1.name)  # main object name changed

           