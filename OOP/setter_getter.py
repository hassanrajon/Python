class Atm:
    def __init__(self):
        self.__pin="" # encapsulation
        self.__balance=0 #encapsulation
    def set_pin(self,new_pin):
        if(type(new_pin)==str):
            self.__pin=new_pin
            print("pin set successfully")
        else:
            print("not valid")
    def get_pin(self):
        print("your pin is "+self.__pin)  
dbbl = Atm()           
dbbl.set_pin("022")           