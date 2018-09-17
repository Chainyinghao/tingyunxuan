# -*- coding: utf-8 -*-
# date:2018/9/16
# comment:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def disin_Num(n):             #网上有些代码是错的，但是有些博主看也不看就各种转载，emmmm
    if n == 1:
        print(n)
        return
    elif n <= 0:
        print("Input mistaken number")
        return 0
    L1 = []
    print(n,"=",end=" ")
    try:
        while n != 1:
            for i in range(2, int(n+1)):
                if n % i ==0:
                    L1.append(i)
                    n /= i
                    break
    except ValueError:
        print("ERROR")
        raise
    for i in range(0,len(L1)-1):
        print("{} * ".format(L1[i]),end=" ")
    print(L1[-1])
    return

nn = eval(input("Input your number:"))
if not isinstance(nn, int):
    print("Please input correct number!")
else:
    disin_Num(nn)

