# -*- coding: utf-8 -*-
# date:2018/9/28
# comment:递归二分法查找

#模块bisect提供标准的二分法查找，只是想写写，为啥没有每天写呢，感觉到这后面，需要多思考很多东西

def search(sequance, number, lower = 0, upper = None):
    if upper is None:
        upper = len(sequance) - 1
    if lower == upper:
        assert number == sequance[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequance[middle]:
            return search(sequance, number, middle+1, upper)
        else:
            return search(sequance, number, lower, middle)

x = input("输入任意一组整数(空格隔开)：")
seq = x.split(" ")   #这里的话，也就是说在py里面，一个变量可以保存多个值，《python基础教程》赋值那章有
seq = [int(seq[i])for i in range(len(seq))]         #将列表中每个字符值转化为整形
seq.sort()
print(seq)
y = eval(input("输入查找字符："))
print("该字符位于：%s" % (search(seq, y)+1))








