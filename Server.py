import socket
import argparse 
from sys import argv
import sys

parser=argparse.ArgumentParser(description="""This is a basic server program""")
parser.add_argument('port', type=int, help='This is the port to connect to the server on',action='store')
args = parser.parse_args(argv[1:])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#need to bind the local name and port
server_addr = ('', args.port)
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
    #go until no more
    if not data:
        break
    clientSocket.sendall(reverseString(data).encode("utf-8"))
    #close
clientSocket.close()



