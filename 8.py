#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/14
# comment:暂停一秒输出，并格式化当前时间

import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

time.sleep(1)

print(time.ctime())


