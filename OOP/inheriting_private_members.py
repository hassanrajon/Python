class phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.__brand=brand # private data
        self.price=price
        self.camera=camera
class smartphone(phone):
    pass
s = smartphone(20,"apple",13) 
print(s.__brand)
"""
private properties cant be inherited,so 
it will crash

"""        