# Inner class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()  # hemi hi a ngai kher lo.

    def show(self):
        print(self.name, self.roll_no)

    class Laptop:
        def __init__(self):
            self.brand = 'Hpa'
            self.cpu = 'i7'
            self.ram = 8

        def display(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Hpa', 157)
s2 = Student('Rpa', 1)
s2.show()
Student.Laptop().display()  # ti pawh hian a print theih.

s1.show()
lap1 = Student.Laptop()  # outer class hmang khan inner class object kan siam thei a ni.
lap1.display()



