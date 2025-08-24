class Printer:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass
    
    
"""
 Problem:

BasicPrinter is forced to implement scan and fax even though it doesn’t support them.
That’s a violation of ISP.
"""    
class BasicPrinter(Printer):
    def print(self, document):
        print("Printing:", document)

    def scan(self, document):
        raise NotImplementedError("This printer cannot scan")

    def fax(self, document):
        raise NotImplementedError("This printer cannot fax")
