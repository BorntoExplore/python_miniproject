import socket

host=' 172.31.84.250'
port = 8080

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))
print(s.recv(1024).decode())
s.close()