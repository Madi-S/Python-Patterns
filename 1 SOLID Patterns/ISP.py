# ISP - Interface Segregation Principle
# Do not put too much methods in a single class
# The idea is following - break smaller interfaces/classes into smaller ones, because we can define methods in a class, which are not necessary, but yet they will be defined in API
# Of course, we can add comments or raise exceptions in unimplemented methods, but still they are defined in API for this particular class
# YAGNI - You aint gonna need it
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionalPrinter(Machine):
    def print(self, document):
        ...

    def fax(self, document):
        ...

    def scan(self, document):
        ...


class OldFunctionalPrinter(Machine):
    def print(self, document):
        print('Printing the document ...')
        print(document)

    # But imagine that other methods (fax & scan) can not implemented in this particular machine

    def fax(self, document):
        """Not supported"""
        'doing nothing'

    def scan(self, document):
        """Not supported"""
        raise NotImplementedError


# ISP approach
class Printer:
    @abstractmethod
    def print(self, document):
        ...


class Scanner:
    @abstractmethod
    def scan(self, document):
        ...


class Faxer:
    @abstractmethod
    def fax(self, document):
        ...


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        ...  # something meaningful

# Implementation of previous Machine class, which now is a special case class
# When we will need only to copy or only to print, we will use Printer or Scanner as a parent class


class MultiFunctionDevice(Printer, Scanner, Faxer):
    @abstractmethod
    def print(self, document):
        ...

    @abstractmethod
    def scan(self, document):
        ...

    @abstractmethod
    def faxer(self, document):
        ...


class MultiFunctionalMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


if __name__ == '__main__':
    # The adverse consequences of not abiding ISP
    printer = OldFunctionalPrinter()
    printer.print(123)  # ok, works
    printer.fax(123)    # nothing happens
    printer.scan(123)   # oops!
