#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/13
# comment:输入三个整数x,y,z，请把这三个数由小到大输出。


l = []
for i in range(3):
    j = i
    x = eval(input('num %s:' % (j+1)))
    l.append(x)
l.sort()
print(l)


