class shop:
    #! class level variable / static variable
    counter=1
    discount=0.1
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        self.serial_no=shop.counter
        shop.counter+=1 
    @classmethod #class method to change discount if need
    def set_discount(x):
         shop.discount=x   
    @staticmethod # static method,which does not depend on class or object
    def add(x,y):
        return x+y    
print(shop.add(10,20)) #this is class or object independent as it is static method
s1=shop("alu",24)
s2=shop("potol",30)
s3=shop("vendi",21)
print(s3.counter,s2.counter,s1.counter) # all of their counter will be same, because counter is static variable
print("s1 serial = ",s1.serial_no) #serial no is different, because its object variable
print("s2 serial = ",s2.serial_no)
print("s3 serial = ",s3.serial_no)
shop.set_discount(0.20)


 
