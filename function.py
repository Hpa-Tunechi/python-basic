def greet():
    print('Hello buddy')
greet()

# addition
def add(x,y):
    a = x + y
    print(a)
add(2,3)

# multiplication return value
def multi(a,b):
    c = a * b
    return c
result = multi(3,4)
print(result)

# return two values
def add_sub(x,y):
    a = x + y
    b = x - y
    return b, a
result1,result2 = add_sub(1,3)
print(result1)
print('\n', result2)
