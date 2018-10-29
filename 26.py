# -*- coding: utf-8 -*-
# date:2018/10/29
#comment:socket,client定时发送时间给server，并且server将时间格式化

#server
import socket
import time
s = socket.socket()  #实例一个socket

s.bind(('127.0.0.1', 8889)) #绑定IP和端口

s.listen()

conn, add = s.accept() #接收到一个连接以及这个连接的地址
print(add)
while True:
    ret0 = conn.recv(1024).decode('utf-8')
    ret1 = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(eval(ret0)))
    print(ret1)
conn.close()  #关闭本次连接

s.close()   #关闭这个socket


#client
import socket
import time
s = socket.socket()

s.connect(('127.0.0.1', 8889))   #建立连接
while True:
    ret = time.time()
    print(ret)
    s.send(bytes(str(ret), encoding='utf-8'))
    time.sleep(10)
s.close()
