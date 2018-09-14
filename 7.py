#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/14
# comment:输出 9*9 乘法口诀表

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(i, j, i*j), end=",")
    print()