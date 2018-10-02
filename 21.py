# -*- coding: utf-8 -*-
# date:2018/10/2
# comment:设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

import functools
import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        oldTime = time.time()
        result = func(*args, **kwargs)
        newTime = time.time()
        print("函数{}执行时间为：{:.3f}" .format(func.__name__, newTime - oldTime))
        #用time.process_time()这个函数会出蜜汁bug,oldTime和newTime相同，但是用time.time（）精度太高，所以需要处理

        return result
    return  wrapper

@log
def fast(x, y):
    time.sleep(0.001)
    return x + y ;

@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f == 33 and s == 7986:
    print("测试成功")
else:
    print("测试失败")

