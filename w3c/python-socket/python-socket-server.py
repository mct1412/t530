#!/usr/bin/python
# coding=utf-8

import socket

s = socket.socket()

host = socket.gethostname()
#host = "localhost"
print(host)
port = 12345
s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print(addr)
    #print("连接地址addr = " + addr)
    c.sendall(("Hello there!").encode())
    c.close()

exit()
