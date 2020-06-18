a = int(input('Enter any number: '))
x = a % 2
if x == 0:
    print(a, ' is even number.\n')
    if a < 5:
        print(a, ' is smaller than 5')
    else:
        print(a, ' is greater than 5')
else:
    print(a,' is odd number')
    if a < 5:
        print(a, ' is smaller than 5')
    else:
        print(a, ' is greater than 5')

