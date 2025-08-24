class car:
    def __init__(self):
        print("this is car class")
class fourwheel(car):
    def __init__(self):
        super().__init__()  
        print("this car has 4 wheel")
class BMW(fourwheel):
    def __init__(self):
        super().__init__()
        print("BMW is a car , which have 4 wheel")              
bmw=BMW() # multilevel inheritance
       