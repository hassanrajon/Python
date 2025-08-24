from abc import ABC,abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self,document):
        pass
class Scanable(ABC):
    @abstractmethod
    def scan(self,document):
        pass    
class Faxable(ABC):
    @abstractmethod
    def fax(self,document):
        pass 

class BasicPrinter(Printable):
    def print(self, document):
        print("printing ",document)  

class AdvancePrinter(Printable,Scanable,Faxable):
    def print(self, document):
        print("printing ",document)
    def scan(self, document):
        print("printing ",document)
    def fax(self,document):
        print("faxing ",document)               

"""
BasicPrinter only implements Printable.

AdvancedPrinter implements multiple capabilities.

No one is forced to depend on unused methods.

 interface segregation respected.
"""       