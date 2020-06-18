# anonymous function | Lambda in python
def square(a):
    print(a*a)
square(5)

# square Using Lambda
g = lambda a: a*a
result = g(5)
print(result)

# addition using lambda
f = lambda a,b: a+b
result = f(3,2)
print(result)

