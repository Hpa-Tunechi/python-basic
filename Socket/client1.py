import socket

c = socket.socket()
c.connect(('localhost', 9997))

message = input('Your message:')
c.send(bytes(message, 'utf-8'))

rec_msg = c.recv(1024).decode()

def msg():
    print(rec_msg)
    msg = input('Your new message: ')
    c.send(bytes(msg, 'utf-8'))


if rec_msg != '':
    msg()
