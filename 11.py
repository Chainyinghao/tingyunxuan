# -*- coding: utf-8 -*-
# date:2018/9/16
# comment:打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。

def daff_Nmum(m, n):
    for i in range(m, n):
        a = int(i / 100)
        b = int(i % 100 / 10)
        c = int(i % 100 % 10)
        if i == (pow(a, 3) + pow(b, 3) + pow(c, 3)):
            print(i)

daff_Nmum(100,1000)
