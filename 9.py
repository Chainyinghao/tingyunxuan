# -*- coding: utf-8 -*-
# date:2018/9/14
# comment:古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


def birth(n):
    __f1__ = 1
    __f2__ = 1
    for i in range(1, n+1):
        print("%d  %d" %(__f1__, __f2__), end="  ")
        if n % 3 == 0:
            print()
            __f1__ += __f2__
            __f2__ += __f1__

    return
j = eval(input("Input the month:"))
birth(j)





