class Area:
    def __init__(self):
        pass
    def area(self,radius,length=0,side=0):
        if(length==0 and side ==0):
            print("area of circle is : ",3.1416*radius**2)
        elif(side==0):
             print("area is : ",radius*length)
        else:
            print("volume is : ",radius*length*side)
ar = Area()
ar.area(10)
ar.area(10,5) 
ar.area(10,10,10)                   