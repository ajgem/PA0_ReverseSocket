import socket

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 6543))
s.listen(5)

while True:
    clientSocket, clientAddress = s.accept()
    print('New connection:', clientAddress)

    message = []
    while True:

        data = clientSocket.recv(2048)
        if not data:
            break
        message.append(data)

    clientSocket.sendall(b''.join(message))
    clientSocket.close()

