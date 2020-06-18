from numpy import *

# matrices

a = array([
    [1,2,3],
    [4,3,2]
])
m = matrix(a)
print(m)

n = matrix('1 2 3 ; 4 3 2')
print(n)

# Diagonal print
print(diagonal(a))
print(n.min())
re = n.reshape(2,3)
print(re)

# addition and multiplication matrix

i = matrix('2 3 4 ; 2 2 2')
j = matrix('1 1 1 ; 2 2 2')
k = i + j
print(k)

l = matrix('2 3 4 ; 2 1 5 ; 6 2 3')
m = matrix('1 3 2 ; 5 7 4 ; 8 3 2')
o = l * m
print(o)
