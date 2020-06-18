# continue hi chu skip na pass ah hi cuan pass tawp pawh a dah theih
a = 10
for i in range(a):
    if i%2 == 0:
        continue
    else:
        print(i,end=' ')

print('\n')

for i in range(a):
    if i%2 == 0:
        pass
    else:
        print(i)

for i in range(a):
    continue
print('hei continue:')
for i in range(a):
    pass
print('hei hi pass:')
