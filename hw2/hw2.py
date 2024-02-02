import os
from socket import *
import sys

serverPort = int(sys.argv[1])

print('Student ID : 20215209')
print('Name : MINA YOON')

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(2048)

    # GET
    if request.startswith(b'GET '):
        request = request.strip()
        filename = request.split()[1]
        try:
            with open(filename, 'rb') as file:
                content = file.read()
                connectionSocket.send(content)
        except FileNotFoundError:
            connectionSocket.send(b'FILE NOT FOUND\r\n')
    # PUT
    elif request.startswith(b'PUT '):
        header = request.split(b'\n', maxsplit=1)
        filename = header[0].split()[1].decode()
        data = header[1]
        with open(filename, 'wb') as file:
            file.write(data)
            while True:
                data = connectionSocket.recv(2048)
                if not data:
                    break
                file.write(data)
                file.flush()
    # LS
    elif request.startswith(b'LS '):
        ext = request.split()[1].decode()
        files = []
        for f in os.listdir('.'):
            if f.endswith(ext):
                files.append(f)
        if files:
            for f in files:
                response = f + '\r\n'            
                connectionSocket.send(response.encode())

    sys.stdout.flush()
    connectionSocket.close()

    
