def update(x):
    x = 8
    print(x)
a = 10
update(a)
print('a =',a)

def hpa(c):
    c = 'tunechi'
    return c
a = 'hpa'
b = hpa(a)
print(a)
print(b)

# list ah kha chuan a pa2 in a in update ve ve ang
def update(lst):
    lst[1]=3
    print(lst)
lst = [1,2,4]
update(lst)
print(lst)