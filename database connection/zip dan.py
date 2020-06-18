# zip kan tih chuan variable pahnih a in zawn a mi print rual dan.

names = ('hpa', 'tunechi', 'hpa tunechi')
ability = ('web developer', 'rapper', 'nothing')

# zipped = list(zip(names, ability)) # list a print dan
# zipped = set(zip(names, ability))  # set a print dan. A in ang a awm pawn pakhat zawk chiah
# zipped = tuple(zip(names, ability))  # tuple a print dan.
# zipped = dict(zip(names, ability))  # dictionary type a print dan.

zipped = zip(names, ability)   # print dan pangai
for i, j in zipped:
    print(i, ':', j)
