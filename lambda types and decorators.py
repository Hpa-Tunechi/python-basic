# lambda types
# filter(), map(), reduce()

# filter()
def even(n):
    return n%2 == 0
nums = [3,4,2,5,6,8]
evens = list(filter(even, nums))
print(evens)
for i in evens:
    print(i, end=' ')

# filter with lambda
nums = [2, 3, 1, 4, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print('\n', evens)

# map with lambda
nums = [2, 3, 1, 4, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n*2, evens))
print(double)


# reduce
from functools import reduce
def add_all(a,b):
    return a + b
no = [3,34,23,12,35]
even_no = list(filter(lambda n: n%2==0,no))
doubles = list(map(lambda n:n*2,even_no))
sum = reduce(add_all,doubles)
print(sum)

# reduce with lambda
from functools import reduce
a = [2,1,4,5,3]
b = list(filter(lambda n:n%2==0,a))
d = list(map(lambda n:n*2,b))
print(d)
sum = reduce(lambda a,b:a+b,d)
print(sum)

# Decorators
# without decorators
def div(a,b):
    if a<b:
        a,b=b,a
        print(a/b)
div(2,4)

# with decorators
def div(a,b):
    print(a/b)
def check(ab):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return ab(a,b)
    return inner
ans = check(div)
ans(8,8)


