import socket
import argparse
from sys import argv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#need to bind the local name and port
port = 5444
server_addr = ("", port)
s.bind(server_addr)
s.listen(5)
#while there is a connection
while True:
    clientSocket, clientAddress = s.accept()
    print('New connection:', clientAddress)

    message = []
    while True:

        data = clientSocket.recv(512)
        if not data:
            break
        message.append(data)

    clientSocket.sendall(b''.join(message))
    clientSocket.close()

clientSocket.close()
