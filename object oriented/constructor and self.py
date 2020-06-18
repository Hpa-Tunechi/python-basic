# constructor and self

# object kan siam apiang khan space tharah a in allocate thin.
class New:
    pass


c1 = New()
print(id(c1))


# update dan kan lo zir ang
class Update:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update(self):
        self.age = 25
        print('name:',self.name, 'age:',self.age)


a = Update('Hpa', 20)
a.update()

# a dan dang chiin aw
class Exupdate:
    def __init__(self):
        self.name = 'rpa'
        self.age = 29
    def exup(self):
        self.age = 30
        print('name:',self.name, 'age:', self.age)
b = Exupdate()
b.name = 'John'
b.exup()
