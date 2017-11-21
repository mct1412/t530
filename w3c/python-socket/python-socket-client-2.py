#!/usr/bin/python
# -*- coding: utf-8 -*-

# client 2

from socket import *

hostname = ""
port = 12346
bufsize = 1024

c = socket(AF_INET,SOCK_STREAM)
#c.settimeout(5)
c.connect((hostname,port))

while True:
    data = input("> ")
    if not data:
        break
    c.send(data.encode())

    data2 = c.recv(bufsize).decode()
    if data2:
        print(data2)
c.close()
