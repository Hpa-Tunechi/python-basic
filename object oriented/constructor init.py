# Constructor = __init__ (init hi constructor a ni)

class Computer:
    # __init__ function will call automatic
    def __init__(self):
        print('tunechi')

    def config(self):
        print("hpa")


com1 = Computer()
com1.config()


# init hmanga value pass dan, init kha a chungah pawh a hnuaiah pawh a dah theih a ni.
class Comp:
    def details(self):
        print('Details of my Computer is', 'cpu =', self.cpu, ' ram =', self.ram)

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


com2 = Comp('intel i5', '8gb')
com3 = Comp('amd', '16gb')
com2.details()
com3.details()