# -*- coding: utf-8 -*-
# date:2018/9/17
# comment:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

from functools import reduce       #听说Mr Guido大大不喜欢reduce这个累积函数？？？所以删了它的全局命名空间不能像2.x版本直接使用了，emmm
def cir_Num():
    temp = 0
    Sn = []
    a = eval(input("Input the basic_num: "))
    n = eval(input("Input the amounts:"))
    for i in range(n):
       temp += a
       Sn.append(temp)
       a = a * 10
    print("sum = ", end=" ")
    for i in range(n-1):
        print("{} + ".format(Sn[i]), end=" ")
    print(Sn[-1])
    Sn = reduce(lambda x, y: x + y, Sn)  # 感觉这里用lamba函数是很骚的操作，参考别人的
    print("    = %d" % Sn)

cir_Num()

