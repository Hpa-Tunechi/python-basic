# Socket programming in python
import socket  # socket import na


s = socket.socket()  # socket siamna lai tak. socket() chhungah hian TCP te, udp network te, IP v4 leh Ip
# v6 te kan duh chuan kan mention thei.

print('Socket created')

# server socket a kan siam dawn khan
s.bind(('localhost', 9998))  # port number kan siam

# start listening to client chu kan tan dawn a ni.
# pathum connection nghak duh ta ila.
s.listen(3)
print('Waiting for connections')

# client hrang hrang connection kha lo accept tur chuan.
while True:
# client atanga connection accept na
    c, addr = s.accept()  # c hi client tih na a nia. addr hi client addresss a ni.

    name = c.recv(1024).decode()

    print('Connected with', addr, name)  # client address kha kan print ang


    # bytes format a kan dah angai send tur chuan.
    c.send(bytes('Welcome to Hpa','utf-8'))  # hei hi client a, a va send tur kha a ni.

    c.close() # client kha kan close ang