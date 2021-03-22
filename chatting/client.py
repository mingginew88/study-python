import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 8000))

name = None

while True:
    read, write, fail = select.select((socket.socket(), server), (), ())

    for desc in read:
        if desc == server:
            data = server.recv(2048)
            print(data.decode())

            if name is None:
                name = data.decode()
                server.send(f'{name} is connected!'.encode())
        else:
            msg = desc.readline()
            msg = msg.replace('\n', '')
            server.send(f'{name} {msg}'.encode())




