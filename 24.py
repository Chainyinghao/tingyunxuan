# -*- coding: utf-8 -*-
# date:2018/10/29
#comment:socket

#server
import socket

s = socket.socket()  #实例一个socket

host = socket.gethostname()
port = 8080
s.bind((host, port)) #绑定IP和端口

s.listen()

conn, add = s.accept() #接收到一个连接以及这个连接的地址
ret = conn.recv(1024)   #接收内容
print(ret)
conn.send(b'hello,client') #发送内容，必须类型为bytes

conn.close()  #关闭本次连接

s.close()   #关闭这个socket


#client
import socket

s = socket.socket()

host = socket.gethostname()
port = 8080

s.connect((host, port))   #建立连接
s.send(b'hello,server')
ret = s.recv(1024)
print(ret)

s.close()
