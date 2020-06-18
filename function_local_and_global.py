# Global and local variable in python
a = 10
print('Local variable and global variable')
def call():
    a = 17
    print('Inside function:',a)
call()
print('Outside function:',a)


# "global" hman dan - local variable value kha local chhungah khan global keyword hmangin kan update thei
b = 10
print('"global" hman dan - We can update global variable inside local variable using "global keyword".')
def update():
    global b
    b = 17
    print('Inside function:',b)
update()
print('Outside function:',b)

# "globals" hman dan
ab = 5
print('"globals" hman dan')
def bals():
    ab = 4
    x = globals()['ab']
    print('inside function but value of global variable:',x)
    print("inside function:",ab)
    globals()['ab'] = 7
bals()
print('outside function:',ab)