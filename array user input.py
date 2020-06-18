from array import *

arr = array('i', [])
a = int(input('Enter the length of an array: '))
for i in range(a):
    b = int(input('Enter the value: '))
    arr.append(b)
for j in range(len(arr)):
    print(arr[j])
search = int(input('Enter number you want to search: '))
for e in range(len(arr)):
    if arr[e] == search:
        print(search,' is found at address', arr.index(search), id(search))
        break
else:
    print(search,'is not found')