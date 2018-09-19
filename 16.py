# -*- coding: utf-8 -*-
# date:2018/9/19
# comment:画一条蟒蛇，今天想复习一下海龟绘图


import turtle

turtle.setup(650, 350, 200, 200)   #额，将就看看吧1
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

