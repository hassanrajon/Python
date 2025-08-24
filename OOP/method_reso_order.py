class A:
    def show(self):
        print("This is class A")

class B(A):
    def show(self):
        print("This is class B")

class C(A):
    def show(self):
        print("This is class C")

class D(B, C):
    pass

d = D()
d.show() # here it shows class b, because of class D inherits B first

