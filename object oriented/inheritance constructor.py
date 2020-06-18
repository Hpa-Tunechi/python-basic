# Constructor in Inheritance
# class A:
#     def __init__(self):
#         print('Inside A init')
#
#     def f1(self):
#         print('Feature A working')
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()  # hemi kan dah chuan super class a mi init kha a va call zel ang
#         print('Inside B init')
#
#     def f2(self):
#         print('Feature 3 working')
#
#
# # a1 = A()
# # a1.f1()
#
# a2 = B()  # hetia object siam ringawt pawh hian init kha a call
# # a2.f2()
# # a2.f1()


# Multiple inheritance
class A:
    def __init__(self):
        print('Inside A init')

    def f1(self):
        print('Class A')


class B:
    def __init__(self):
        print('Inside B init')

    def f2(self):
        print('Class B')


class C(A, B):
    def __init__(self):
        super().__init__()  # hei hian super class left zawk init chiah hi a call ve ang.
        print('Inside C init')

    def f3(self):
        print('Class C')


c = C()  # hei hian subclass A leh B a nia class a a left a awm zawk init khi a call ve ang, a ma init nen.
c.f1()
c.f2()
c.f3()

a = A()
a.f1()
