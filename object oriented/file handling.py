# File handling
                                # READ
f = open('text.txt', 'r')  # kan file open na.
# print(f.read())  # hei hian a vaiin a print ang
# print(f.readline())  # a line a print na.
# print(f.readline())


                                # WRITE
# tunah chuan write dan - Write hi chuan a hmasa awm kha a overwrite tawp dawn ani..
# Chu chu a hmasa a mi kha a bo vek ang.
# f1 = open('abc.txt', 'w')  # write hi chuan file a awm sa leh sa loh a en anga, a awmsa loh chuan a siam chawp ang.
# f1.write('Something bitch')


                                # APPEND
# 'write' ah khan chuan a overwrite tawp avang khan 'append' hi kan hmang ang chhun zawm nan.
f1 = open('abc.txt', 'a') # 'a' hi append tihna a ni.
f1.write('Hpa') # a tawp lamah khan a va zawm dawn a ni hei hi chuan.

            # a dawt te te a print kha a theih tho a ni.
# for data in f:
#     print(data)

                # data kan write chhawn dan tur
for data in f:
    f1.write(data)


                                # Thlalak lampang ve thung aw.
a = open('hpa.jpg', 'rb') # rb = read binary tih na a ni.
# for i in a:
#     print(i)  # hei hian kan thlalak code a kha a print ang.

                                # Thlalak copy dan.
b = open('hpapic.jpg', 'wb')  # wb = write binary a ni.

for i in a:
    b.write(i)

                                # comment
    # hash hi line anga commentna a n a, """ hei hi documentation kan tih chauhin comment nan kan hmang ang.
# example for hash
""" 

example for documentation.

"""