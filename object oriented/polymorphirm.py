# Polymorphism - One to many
# One thing can take multiple form, object will have multiple forms.
# Four types of Polymorphism
# 1) Duck typing
# 2) Operator Overloading
# 3) Method Overloading
# 4) Method overriding

# 1) Duck typing
# Hetah hi chuan class pakhat chhung atangin class dang chhung a mi kha kan va call ang.


class Pycharm:
    def execute(self):
        print('Compiling 1')
        print('running 1')


class MyEditor:
    def execute(self):
        print('Spell check')
        print('Convention check')
        print('compiling')
        print('running')


class Laptop:  # Hemi class ah hian object method kan nei a chu chuan class danga mi kha kan call thei a ni.
    def code(self, i, j):
        i.execute() # hei hian a han call dawn a ni.
        j.execute()


i = MyEditor()
j = Pycharm()
lap1 = Laptop()
lap1.code(i, j)


# 2) operator overloading
# Operator overloading ah chuan operator kha a ngai reng anga, operands chu chu a value te kha a dang ang.
# Operator overloading kan tih chuan object kan siam hmang khan operator kha a work tawp thei lova. chuvang chuan
# a work theih nan khan kan class chhungah khan method kan va call anga khami hmang khan a work dawn a ni.
a = 3
b = 2
print(a + b)  # hemi behind a a work dan chu a hnuai a mi ang hi a ni.
print('add dan awlsam:', int.__add__(a, b))  # __add__ hi method a ni.


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):   # __add__ hi method a ni.
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):  # gt chu greater than method tih na mai a ni. tah hian compare na kan nei dawn nih chu.
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self): # string method a ni
        return '{} + {}'.format(self.m1, self.m2)  # String kan return na kha a ni.


s1 = Student(1, 2)
s2 = Student(3, 6)
a = s1 + s2  # helaia addition hi class chhunga __add__ method khian a ti work dawn a ni.
print(a.m2)

if s1 > s2:  # hei hi work tur chuan class chhungah khian __gt__(greater than khi kan call a ngai leh ta a ni.)
    print('s1 is wins at:', s1) # helaia s1 value hi display thei tur chuan __str__ khi kan call leh a ngai ta bawk ani.
else:
    print('s2 is wins at:', s2)


# 3. Method overloading
# class pakhatin method pahnih hming in ang mahse parameter lak zat in ang lo.
# Eg: class Student:  class pakhat hian method pahnih hming in ang a nei a mahse parameter zat in ang lo.
#           def  average(a,b):
#           def average(a,b,c):

class Addition:
    def sum(self, a=None, b=None, c=None):  # parameter ah khan dah kim vek lo mahse None ah khan  adah mai dawn a ni.
        s = 0
        if a!=None and b!=None and c!=None:  # hei hi a check na
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

a = Addition()
print(a.sum(2,3))  # parameter ah hian duh duh zat dah mah ila a print thei dawn a ni.


# 4. Method overriding
# class pakhatin method pahnih hming leh parameter in ang.


class A:
    def show(self):
        print('in A show')


class B(A):  # hemi hian class B in show method a neih loh chuan class A method show hi a han call mai dawn a ni.
    pass
    def show(self):
        print('in B show')

a1 = B()
a1.show()