import socket

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5444))
s.listen(5)

def reverseString(strings):
  return strings[::-1]

clientSocket, clientAddress = s.accept()
print('New connection:', clientAddress)

while True:

    data = clientSocket.recv(2048).decode("utf-8")
    print(reverseString(data))
    if not data:
        break
    clientSocket.sendall(reverseString(data).encode("utf-8"))
    
clientSocket.close()



