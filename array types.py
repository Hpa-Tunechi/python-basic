from numpy import *

a = array([1, 2, 3.5], int)
print(a[0])
print(a.dtype)
# linspace ah hi chuanin start,stop leh step(hei hi a diplay zat tur kha a ni. Chuan a stop value hi a huam tel bawk)
b = linspace(1, 7, 5)
print(b)

# arange ah hian start,stop leh step(hei hi a display karthlak dan tur a ni. Chuan stop value a huam ve lo.)
c = arange(1,7,1)
print(c)

d = logspace(1,10,2)
print(d)

e = zeros(5,int)
print(e)

f = ones(5, int)
print(f)