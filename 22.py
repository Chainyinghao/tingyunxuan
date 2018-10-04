# -*- coding: utf-8 -*-
# date:2018/10/4
# comment:复习一下算法的八皇后问题

'''
关于下列算法的一些注解：可能的所有解或者其中的一部分放在state元组里面，里面每个元素表示相应行中的皇后所处的列，换句话说
比如 state[0] == 3，代表了位于第一行的皇后处于第一行第四列；yield是迭代生成器，调用一次生成一个值，并保存，下一次又重这个位置开始
'''
import random


def conflict(state, nextX): #检测下一个皇后与当前皇后的x坐标是否相同或者是位于同一条对角线上
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            #检测下一个皇后与当前皇后的水平距离是否为0（在同一列）或与他们的垂直距离是是否相等（位于同一条对角线）
            return True
    return False

def queens(num = 8, state=()):  #默认有八个皇后
    for pos in range(num):
        if not conflict(state, pos):#如果没有冲突
            if len(state) == num - 1:#产生当前皇后的位置状态
                yield (pos, )
            else:#否则将当前皇后的w位置添加到元组，并传送给下一皇后
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result  #result代表queens返回的元组

'''
若是最后一行 对于 pos in range(num)调用conflict(state, num)
如果没有冲突,生成元组
若不是最后一行 对于pos in range(num)调用conflict(state, pos)
如果没有冲突,state更新,递归调用queens(num, state) state将更新
'''


def my_print(solution):
    def line(pos, length = len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
    for pos in solution:
        print(line(pos))
print("一共有%s种解法" % (len(list(queens(8)))))
print("其中一种解法为：")
my_print(random.choice(list(queens(8))))