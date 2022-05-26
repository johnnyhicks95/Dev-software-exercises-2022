#!/usr/bin/python3
import socket

#We’ll try to grab banners for ports 21 (ftp), 22 (ssh), 
#25(smtp), and 3306 (mysql).

Ports = [21,  22, 25, 3306]
for i in range(0, 4):
    s=socket.socket()
    Ports=Port[i]
    print("This is the banner for the port")
    print(ports)
    s.connect(("192.168.1.101", Port))
    answer=s.recv(1024)
    print(answer)
s.close()