import socket
import threading

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            break
        print(data)
        c.sendall(data)

s = socket.socket()
s.bind(('127.0.0.1', 5000))
s.listen(5)
print("Waiting for connections")

try:
    while True:
        c, a = s.accept()
        print("COnnected", a)
        t = threading.Thread(target=handle, args=(c,))
        t.start()
except KeyboardInterrupt:
    s.close()
