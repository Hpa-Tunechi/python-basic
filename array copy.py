from numpy import *

arr = array([1,2,3,4])
arr = arr + 2
print(arr)

arr1 = array([1,2,3,4])
arr2 = array([2,3,1,2])
arr3 = arr1 + arr2
print(arr3)

print(sum(arr1))
print(sin(arr1))
print(min(arr1))
print(max(arr1))
print(sqrt(arr1))
print(concatenate([arr2,arr3]))
print(id(arr1))
print(id(arr2))
arr1 = arr2
print(id(arr2))
print(id(arr1))
arr3 = arr2.view()
print(id(arr3))
print(id(arr2))

# Shallow copy ah chuan a value khawi zawk2ah pawh thlak ila a pahnih in a in thlak zel ang.
a = array([3,2,4])
b = a.view()
b[1] = 28
print(a,'\n',b)
print(id(a))
print(id(b))

# deep copy ah chuan a value pa1 thlak khan pa1 zawk a effect lo.
c = array([43,23,2])
d = c.copy()
c[1] = 8
print(c)
print(d)
print(id(c))
print(id(d))
