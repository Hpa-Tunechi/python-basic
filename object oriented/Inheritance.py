# inheritance
# class A:  # super class
#     def feature1(self):
#         print('Feature 1 working')
#
#     def feature2(self):
#         print('Feature 2 working')
#
#
# class B(A):  # sub class/child class
#     def feature3(self):
#         print('Feature 3 working')
#
#     def feature4(self):
#         print('Feature 4 working')
#
#
# a1 = A()  # super class atang hi chuan super class chhung a mi chiah kan call thei sub class/child class a mi chu theih ve loh
# a1.feature1()
# a1.feature2()
# a2 = B()  # sub class/child class atang hi chuan super class kha kan call thei.
# a2.feature3()
# a2.feature4()
# a2.feature1()
# a2.feature2()


# Multilevel Inheritance - multilevel ah chuan super class a awm a sub class khan sub class a nei chhawng leh.
# class A:  # super class
#     def feature1(self):
#         print('Feature 1 working')
#
#     def feature2(self):
#         print('Feature 2 working')
#
#
# class B(A):  # A sub class/child class
#     def feature3(self):
#         print('Feature 3 working')
#
#     def feature4(self):
#         print('Feature 4 working')
#
#
# class C(B):  # B sub class/child class
#     def feature5(self):
#         print('Feature 5 working')
#
#
# a1 = A()  # super class a nia a ma class chhung a mi chiah a call thei.
# a1.feature2() # hei aw
# a2 = B()  # A sub class/child class a nia A leh B class chhung a mi chiah a call thei.
# a2.feature1()  # hei aw
# a3 = C()  # B sub class/child class a nih avangin A leh B leh a mah B class a mi zawng2 a call vek thei.
# a3.feature1()
# a3.feature2()
# a3.feature3()
# a3.feature5()


# Multiple inheritance - Multiple inheritance ah chuan super class pahnih khan sub class in ang an nei ang.
class A:  # super class
    def f1(self):
        print('class A')


class B: # super class
    def f2(self):
        print('class B')


class C(A, B): # super class
    def f3(self):
        print('class C subclass of A and B')


a1 = A()  # class A a nia a chhung a mi chauh a call thei
a1.f1()
a2 = B()  # class B a nia a chhung a mi chiah a call thei
a2.f2()
a3 = C()  # class C a nia class A leh B subclass a nih avangin a call thei vek.
a3.f1()
a3.f2()
a3.f3()
