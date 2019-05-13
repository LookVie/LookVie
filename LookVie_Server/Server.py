import socket

import socketserver

import os

import sys

HOST = 'localhost'

PORT = 5000

ADDR = (HOST,PORT)

BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)

serv.listen(5)

print("server running")

conn, addr = serv.accept()




print("client connected",addr)

conn.sendall(bytes("HELLOWORLD\n",'UTF-8'))

while True:

    recvData = conn.recv(1024)
    print('상대방 :', recvData.decode('utf-8'))

    sendData = input('>>>')
    conn.sendall(bytes(sendData+'\n','UTF-8'))


    


conn.close()

serv.close()

