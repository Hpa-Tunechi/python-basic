# function variable length

def data(*all):
    print(all)
    for i in all:
        print(i)
data('hpa',23,9862532167)

# ** star pahnih hian keyword pawh kha a dawng thei a ni.
def details(**all):
    for i,j in all.items():
        print(i,j)
details(name='hpa',age=25,phone=8974435939)