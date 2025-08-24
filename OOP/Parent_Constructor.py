class phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.brand=brand
        self.price=price
        self.camera=camera
class smartphone(phone):
    pass
s = smartphone(20,"apple",13) 
"""
here smartphone class dont have any constructor, 
so it used its parent class's constructor

"""        