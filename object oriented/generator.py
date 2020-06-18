# generator
# generator will give you iterator


def topten():

    yield 1  # yield hi kan function kha generator a siam tu a ni. return ang thovin iterator kha a return ve ang.
    yield 2
    yield 3

values = topten()
print(values) # kan value print tur cuan next kha kan hman angai.
print(values.__next__())  # iterator print tur chuan __next__ hi kan hman angai.
print(values.__next__())

for i in values:
    print(i)


# square 10 thleng kan print ang
def square():

    n = 1
    while n <= 10:
        sq = n*n
        yield sq # iterator value return nana kan hman kha a ni yield hi.
        n += 1

a = square()
for i in a:
    print(i)