#!/usr/bin/python
# -*- coding: utf-8 -*-

# server 2

import socket
from time import ctime

hostname = ""
port = 12346
bufsize = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.settimeout(10)
s.bind((hostname,port))
s.listen(5)


while True:
    print("waiting for connection ...")
    c,addr = s.accept()
    print("recieve from addr : ", addr)

    while True:
       data = c.recv(bufsize).decode()
       if not data :
          print("break")
          break 
       data2 = ("[%s] %s" % (ctime(),data)).encode()
       #c.send(("[%s] %s" % (ctime(),data)).encode())
       c.send(data2)

c.close()
s.close()

