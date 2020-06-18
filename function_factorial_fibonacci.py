# Pass List to a Function
lst = [23,1,3,5,2,18]


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)
print('count of even:', even, '\n', 'count of odd:', odd)


# Fibonacci
n = int(input('Enter no.:'))
def a(no):
    a = 0
    b = 1
    print(a, b, end=' ')
    for i in range(2,no):
        c = a + b
        a = b
        b = c
        print(c, end=' ')
a(n)

# Factorial

a = int(input('\nEnter value you wanna factorial:'))
def fac(a):
    f = 1
    for i in range(1, a+1):
        f = f * i
    return f, i
fac, i = fac(a)
print('\nfactorial of',i,'is',fac)

