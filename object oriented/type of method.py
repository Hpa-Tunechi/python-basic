# Three types of method
# 1.instance method
# 2. class method
# 3. static method

# 1. instance method
# a) accessor - data lak(fetch) nan kan hmang
# b) mutator - data modify(thlak) nan kan hmang

#
# class student:
#     school = 'Hpa'
#
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     def get_m1(self):  # Accessor
#         return self.m2
#
#     def set_m1(self, value):  # Mutator
#         self.m2 = value
#
#
# s1 = student(32, 43, 53)
# s2 = student(34, 25, 24)
# print(s1.avg(), s1.school)  # instance method
# print(s2.avg())  # instance method
#
# s1.set_m1(12)  # mutator
# print(s1.get_m1())  # accessor


# 2. class method - if you change others will change
# class Student:
#     school = 'Hpa'
#
#     def __init__(self, m1, m2, m3): # instance variable kan access dawn chuan self angai.
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     @classmethod  # class method hman dawn chuan @classmethod decorator hi hman angai.
#     def info(cls): # Class variable kan hman dawn chuan cls hman tur.
#         return cls.school
#
#
# s1 = Student(23, 53, 23)
# s2 = Student(23, 23, 21)
#
# print(s1.avg())
# print(Student.info())


# 3. static method
class Student:
    school = 'Hpa'
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is student Class')


s1 = Student(23, 53, 23)
s2 = Student(23, 23, 21)

print(s1.avg())
print(Student.getSchool())
Student.info()