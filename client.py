import socket
import sys

SERVER_PORT = int(sys.argv[1])
SERVER_IP = sys.argv[2]
PATH = sys.argv[3]
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
TIME_TO_REACH_SERVER = float(sys.argv[4])
try:
    ID = sys.argv[5]
except IndexError:
    ID = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.2.5',12345))
s.send(b'David Gurovich')
data = s.recv(100)
print("Server sent: ", data)
s.send(b'318572047')
data = s.recv(100)
print("Server sent: ", data)
s.close()
