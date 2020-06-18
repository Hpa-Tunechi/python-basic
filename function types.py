# position argument
# position ah chuan a value pass na zawn2 a mi kha a lo dawn tur chu a ni mai.

def add(name,age):
    print(name, age)
add(23,'hpa')

# keyword argument
# a keyword tel khan kan pass ang.
def a(name, age):
    print(name)
    print(age)
a(age=23,name='hpa')

# default argument ah chuan a default kan dah sa ang. duh chuan value kan pass thei tho, value kan pass loh chuan
def b(name, age=27):
    print(name)
    print(age)
b('hpa',22)

# variable length argument
# variable length argument ah chuan a hlawm a hlawm khan value kan pass thei.
def sum(a,*b):
    print(a,b)
    c = a
    for i in b:
        c = c + i
    print(c)
sum(2,3,4)

def hpa(*b):
    a = 0
    for i in b:
        a = a + i
    print(a)
hpa(1,2,3)
