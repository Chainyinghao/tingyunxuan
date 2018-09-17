# -*- coding: utf-8 -*-
# date:2018/9/15
# comment:判断101-200之间有多少个素数，并输出所有素数。

import math
def prime_Num(m, n):   #难受，10、11、12不小心被我弄没了，啊啊啊，重写吧
    num = 0
    flag = 1
    for i in range(m, n+1):
        j = int(math.sqrt(i))
        for k in range(2, j+1):
            if i % k == 0:
                flag = 0
                break
        if flag == 1 :
            print("%d " % i,end=" ")
            num += 1
        flag = 1
    print("\nThe total numbers: %d" % num)

prime_Num(101, 200)

