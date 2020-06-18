## Recursion - recursion chu function call itself
# def a():
#     print('Hello recursive function\n')
#     a()
# a()

## Recursion set limit
# import sys
# print(sys.getrecursionlimit())

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i = 0
# def greet():
#     global i
#     i += 1
#     print("Hello", i)
#     greet()
# greet()

# Factorial using recursion
def call():
    n = int(input('Enter no you wanna factorial using recursion:'))
    def a(n):
        if n == 0:
            return 1
        return n * a(n-1)
    result = a(n)
    print(result)
    call()
call()