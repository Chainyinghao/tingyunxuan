#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/14
# comment:斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


def feb(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return feb(n-1)+feb(n-2)
print(feb(10))
