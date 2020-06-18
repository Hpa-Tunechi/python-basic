# Two types of variables in Class
# 1) Instance variable
# 2) Class(static) variable

# 1) Instance Variable
class Car:
    def __init__(self):
        self.mile = 10
        self.model = 'maruti 800'


c1 = Car()
c1.mile = 20
c1.model = 'Bugati'
c2 = Car()

print(c1.mile, c1.model)
print(c2.mile, c2.model)


# 2) Class(static) Variable
class Taxi:
    wheels = 4 # inside a declare dan

    def __init__(self):
        self.mile = 10
        self.model = 'Hero'


c1 = Taxi()
c2 = Taxi()
c2.mile = 20
c2.model = 'suzuki'
# Taxi.wheels = 5 outside class a declare dan

print('Miles', c1.mile, 'model', c1.model, 'Wheels', c1.wheels)
print('Miles', c2.mile, 'model', c2.model, 'Wheels', c2.wheels)