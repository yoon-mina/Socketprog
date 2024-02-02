import os
import sys
from socket import *

serverPort = int(sys.argv[1])

print('Student ID : 20215209')
print('Name : MINA YOON')

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

def fileType(filename):
    if filename.endswith(".html"):
        return "text/html"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".jpg"):
        return "image/jpeg"
    else:
        return "application/octet-stream"

while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(2048).decode()

    # GET
    if request.startswith('GET '):
        request_lines = request.strip().split('\n')

        print(request_lines[0])
        sys.stdout.flush()
        for line in request_lines[1:]:
            if 'Host:' not in line:
                print(line)  
                sys.stdout.flush()

        filename = request_lines[0].split()[1][1:]

        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                content = f.read()
                header = f'HTTP/1.0 200 OK\r\nConnection: close\r\nContent-Length: {len(content)}\r\nContent-Type: {fileType(filename)}\r\n\r\n'
                connectionSocket.send(header.encode())
                connectionSocket.send(content)
                print(f'\nFile Transfer Done: Sent {len(content)}, File Size {os.path.getsize(filename)}')
                sys.stdout.flush()
        elif filename != 'favicon.ico':
            error_header = 'HTTP/1.0 404 NOT FOUND\r\nConnection: close\r\nContent-Length: 0\r\nContent-Type: text/html\r\n\r\n'
            connectionSocket.send(error_header.encode())
            print('\nServer Error : No such file ./' + filename + '!')
            sys.stdout.flush()

    f.close()
    connectionSocket.close()