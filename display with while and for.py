a = 1
while a <= 5:
    b = 1
    while b <= a:
        print('#', end='')
        b += 1
    a += 1
    print('')

for i in range(4):
    for j in range(4-i):
        print('#', end='')
    print('')

for i in range(5):
    for j in range(1+i):
        print('@', end='')
    print('')