# -*- coding: utf-8 -*-
# date:2018/10/29
#comment:socket

#server
import socket

s = socket.socket()  #实例一个socket

s.bind(('127.0.0.1', 8889)) #绑定IP和端口

s.listen()

conn, add = s.accept() #接收到一个连接以及这个连接的地址
print(add)
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        break
    print(ret)
    info = input('>>>')
    conn.send(bytes(info, encoding='utf-8'))


conn.close()  #关闭本次连接

s.close()   #关闭这个socket

#client
import socket

s = socket.socket()

s.connect(('127.0.0.1', 8889))   #建立连接
while True:
    info = input('>>>')
    if info == 'bye':
        s.send(b'bye')
        break
    s.send(bytes(info, encoding='utf-8'))
    ret = s.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        s.send(b'bye')
        break
s.close()

