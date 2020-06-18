# compare
class Update:
    def __init__(self):
        self.name = 'hpa'
        self.age = 25

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Update()
c1.age = 25
c2 = Update()

if c1.compare(c2):
    print('equal age')
    print(c1.age)
else:
    print('not')
    print(c1.age)
print(c1.age)