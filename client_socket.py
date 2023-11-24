import socket
import time

s = socket.socket()
s.connect(('127.0.0.1', 5000))

try:

    while True:
        s.sendall(b"HeLLo")
        data = s.recv(1024)
        print(data)
        time.sleep(2)
except KeyboardInterrupt:
    s.close()