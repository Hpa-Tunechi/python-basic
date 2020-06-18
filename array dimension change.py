from numpy import *
a = array([
    [2,3,4],
    [5,9,2],
    [8,2,4],
    [3,53,23]
])
print(a)
print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)

# one dimension a dah leh dan
arr = a.flatten()
print(arr)

# a 2 dimension a dah leh dan
arr1 = arr.reshape(4,3)
print(arr1)
print(arr1.ndim)

# 3 dimension a dah leh dan
arr2 = arr.reshape(2,2,3)
print(arr2)
print(arr2.ndim)
print(len(arr2))
print(arr2.size)