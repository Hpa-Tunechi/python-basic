import socket

s = socket.socket()
print('Socket created')

s.bind(('localhost', 9997))

s.listen(3)
print('waitiing client')

while True:
    c, addr = s.accept()
    msg = c.recv(1024).decode()
    print('Connected with', addr)
    print(msg)
    message = str(input('Any message for client: '))
    c.send(bytes(message, 'utf-8'))

    newmsg = c.recv(1024).decode()
    if newmsg != '':
        print(newmsg)
    c.close()
