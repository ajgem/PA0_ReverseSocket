import socket

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#need to bind the local name and port
port = 5444
server_addr = ('', port)
s.bind(server_addr)
s.listen(5)

def reverseString(strings):
  return strings[::-1]

clientSocket, clientAddress = s.accept()
print('New connection:', clientAddress)

while True:

    data = clientSocket.recv(512).decode("utf-8")
    print(reverseString(data))
    if not data:
        break
    clientSocket.sendall(reverseString(data).encode("utf-8"))
    
clientSocket.close()



