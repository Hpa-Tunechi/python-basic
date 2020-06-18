import socket

c = socket.socket()

c.connect(('localhost', 9997))

# server side a message send dan
name = input('Enter your name')
c.send(bytes(name, 'utf-8'))

# server in a rawn thawn receive dan
print(c.recv(1024).decode())  # b kan tih bo dawn chuan