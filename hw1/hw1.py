import socket 
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = []
while True:
    line = input().strip()  

    if (line):
        if line[-2] != '\r' and line[-1] == '\n':
            line = line[:-1] + '\r\n'
        elif line[-1] == '\r':
            line = line[:-1] + '\r\n'
        elif line == '':
            line = '\r\n'
    message.append(line)

    if line == '' or line == '\r\n':
        break
        
for i in message:
    if i == '\r\n':
        i += '\r\n'
    i = i + '\r\n'
    client_socket.send(i.encode())

message=[]

data = client_socket.recv(2048)
while data:
    print(data.decode(), end="")
    data = client_socket.recv(2048)
data =''

client_socket.close()

