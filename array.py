import array

val = array.array('f',[5,3,23,52])
print(val)

from array import *

a = array('i',[3,53,21,35])
print(a)
print(a.buffer_info())
print(a)
print(len(a))
for i in a:
    print(i, end=' ')
print('')
a.reverse()
for i in range(len(a)):
    print(a[i], end=' ')

val.append(23)
print('\n',val)

# array thar a array value awm tawh sa hman dan

new = array(a.typecode,(i * i for i in a))
for j in new:
    print(j)

a.reverse()
newarray = array(a.typecode, (k*k for k in a))
l = 0
while l < len(newarray):
    print(newarray[l])
    l += 1
