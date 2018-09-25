# -*- coding: utf-8 -*-
# date:2018/9/25
# comment:利用迭代器计算圆周率的值

import itertools

def PI(N):
    l = itertools.count(1, 2)      #创建一个奇数序列
    l_n = itertools.takewhile(lambda x: x <= 2 * N - 1, l)   #取该序列的前2N-1项
    l_n = map(lambda x: (-1)**(x//2) * 4 / x, l_n)   #偶数项取负数，每一项用4除
    return sum(l_n)   #求和

print("{0:.8f}".format(PI(100000)))     #N的值越大，越接近PI的值




