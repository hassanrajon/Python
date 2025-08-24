class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print("Salary:", self.salary)


# Child inherits from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, salary, dept):
        # Initialize both parent classes
        Person.__init__(self, name)
        Employee.__init__(self, salary)
        self.dept = dept

    def show_info(self):
        print("Manager of:", self.dept)


# ---- Testing ----
m1 = Manager("Razon", 50000, "IT")
m1.show_name()     # from Person
m1.show_salary()   # from Employee
m1.show_info()     # from Manager
