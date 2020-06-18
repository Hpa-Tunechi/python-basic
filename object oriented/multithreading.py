# Multithreading
# Task lianpui kha te reuh te te ah kan then a chu mi te reuh te te chu thread chu a ni.

class Hello:
    def run(self):
        for i in range(5):
            print('Hello')

class Hi:
    def run(self):
        for i in range(5):
            print('Hi')

a = Hello()
a.run()
b = Hi()
b.run()

# A rual chiah a run dan kha kan ti dawn a ni chu chu multithreading chu ani dawn ta a ni.
# thread ah kan siam dawn a ni.
# thread kan siam dawn chuan threading kan import a ngaia . chuan sleep kan dah tel nachhan chu a insu buai tur
# venna kha a ni.

# thread kha pathum a awm a, print() a hnuai bera kan dah kha a tawp bera print kan duh chuan a leh b hi kan join phawt
# a ngai dawn a ni.
# 1) main thread
# 2) a
# 3) b

from threading import *  # threading import na kha a ni.
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

a = Hello()
b = Hi()

a.start()  # thread kan run dawn kha chuan start() hi a nih angai.
sleep(1) # collide a awm chuan. entirnan: HelloHi te lo ni rual ta se. sleep(1) kan dah hian a ti awm dwn lo a ni.
b.start()  # tah pawh a nih tho hi.

# print() hi main thread a mi a ni a, a tawp bera print kan duh chuan thread a leh b hi kan join phawt a ngai dawn a ni.
a.join()
b.join()
print('bye')
