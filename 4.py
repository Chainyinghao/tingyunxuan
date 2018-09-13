#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/13
# comment:输入某年某月某日，判断这一天是这一年的第几天？


year = eval(input('year：'))
month = eval(input('month:'))
day = eval(input('day:'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    days = months[month-1]
else:
    print('ERROR')
days += day
flag = 0
if(year % 400 == 0)or((year % 4 == 0)and(year % 100 == 0)):
    flag = 1
if(flag == 1)and(month > 2):
    days += 1
print('all days is: ', days)


