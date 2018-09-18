# -*- coding: utf-8 -*-
# date:2018/9/18
# comment:一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def wan_Num(m, n):
    if m < 2:
        print("The num at least is 2!")
        return -1
    for i in range(m, n+1):
        L1 = []
        count = -1
        s = i                 #因为求的是i的因子，所以后面i的值不能发生变化
        for j in range(1, i):
            if i % j == 0:
                L1.append(j)
                s -= j
                count += 1
        if s == 0 and sum(L1) == i:
            print("%s = " % i, end=" ")
            for k in range(count):
                print("{} +".format(L1[k]), end=" ")
            print("%s" % L1[count])

wan_Num(2,1000)


