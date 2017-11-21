#!/usr/bin/python
# coding=utf-8

import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
s.connect((host,port))

#data = s.recv(1024).decode()
print(s.recv(1024).decode())
#print(data)
s.close()
