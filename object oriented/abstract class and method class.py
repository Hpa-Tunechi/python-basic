# Abstract class and method
#class Computer:
#    def process(self):
 #       pass # Hetia pass kan hman hian blank method a lo ni mai dawn ni. chu chu 'abstract method' a lo ni ang.
                # class in abstract method a neih chuan chu class chu abstract class a lo ni mai dawn a ni.

from abc import ABC, abstractmethod  # hei hi abstract class import na a ni.


class Computer(ABC):  # abstract class hi chu a call theih loh a ni.
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print('Its running')


class Programmer:
    def work(self, com):
        print('Solving Bugs')
        com.process()

# com = Computer()
com1 = Laptop()
# com1.process()
p = Programmer()
p.work(com1)
