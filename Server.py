import socket

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#need to bind the local name and port
port = 5444
server_addr = ('', port)
s.bind(server_addr)
s.listen(5)
#create a reverse functon 
def reverseString(strings):
  return strings[::-1]
#accept the sock and addy
clientSocket, clientAddress = s.accept()
print('New connection:', clientAddress)
#while still receiveing
while True:
#decode the data
    data = clientSocket.recv(2048).decode("utf-8")
    print(reverseString(data))
    #go until no more
    if not data:
        break
    clientSocket.sendall(reverseString(data).encode("utf-8"))
    #close
clientSocket.close()



