# -*- coding: utf-8 -*-
# date:2018/10/24
#comment:json中的dumps

import json

#dumps()
class student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = student('Bob', 12, 90)
#啥意思呢，就是说json可以将一个类序列化，只不过不能直接转
#方法一：就是再写一个函数，将要转化类中的变量先转为dict
def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))

#方法二：方法一那种如果还有其他类的话，就还得写一个转化函数，不方便，但是基本大多数类都默认有__dict__来存储类中的变量，所以通过访问这个达到目的
print(json.dumps(s, default=lambda obj: obj.__dict__))


