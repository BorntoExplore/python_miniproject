import socket

host=' 172.31.84.250'
port = 8080

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(5)

print("Waiting from incoming connection with port: ",port)

while True:
    conn,addr=s.accept()
    print("Got connection from ", addr)
    msg = "Welcome to Server!!"
    conn.send(msg.encode())
    conn.close()