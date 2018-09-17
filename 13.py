# -*- coding: utf-8 -*-
# date:2018/9/17
# comment:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

def count_Function():                     #py大法好，库函数比较多，省事，程序猿怎么能没有API文档呢
    s = input("Input your string: ")
    ch = 0
    space = 0
    num = 0
    other = 0
    i = 0
    while i < len(s):
        Str = s[i]
        if Str.isalpha():
            ch += 1
        elif Str.isspace():
            space += 1
        elif Str.isalnum():
            num += 1
        else:
            other += 1
        i +=1
    print("chars：{},spaces{},numbers:{},others:{}".format(ch, space, num, other))
count_Function()
