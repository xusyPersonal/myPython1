# print("xusy is a mus man");
#
#
# import time
#
# print(time.time() ) #1498539133.655
# print(time.localtime())  #tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1, tm_yday=178, tm_isdst=0
# print(time.asctime())  #'Tue Jun 27 12:53:50 2017'
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #'2017-06-27 13:00:57'
#
# import datetime
#
# print(datetime.date.today()) #datetime.date(2017, 6, 27)
# print(datetime.date.today().strftime('%d/%m/%Y')) #'27/06/2017'
# print(datetime.date(1941, 1, 5)) #datetime.date(1941, 1, 5)
#
# from datetime import *
# import time
#
# #返回当前本地时间
# print("today:"+str(date.today()))
# print("today:"+str(date.fromtimestamp(time.time())));

# score = int(raw_input('输入分数:\n'))
score=20;
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('%d 属于 %s' % (score, grade));


# !/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# !/usr/bin/python3

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print(str);
    return ;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# !/usr/bin/python3

def ChangeInt(a):
    a = [0,8]
b = [9,0]
ChangeInt(b)
print(b)  # 结果是 2


# !/usr/bin/python3

# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name);
    print("年龄: ", age);
    # return;


# 调用printinfo函数
printinfo(age=50, name="runoob") ;

# !/usr/bin/python
# -*- coding: UTF-8 -*-

tmp = 0
for i in range(1, 101):
    tmp += i
print('The sum is %d' % tmp) ;
print('xusy:%d' % 45);
print('' , 23);


#!/usr/bin/python
# -*- coding: UTF-8 -*-

m = 1
n = 100

area = (m+n)*(n-m+1)/2

print ("sum from %d to %d is %d" %(m,n,area)) ;

print (sum(range(1,101)));

def my_sum(x):
    if x == 100:
        return 100
    else:
        return  x + my_sum(x + 1)
print(my_sum(1)) ;

# 0+1+2...+99+100 ;


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# TRUE = 1
# FALSE = 0
# def SQ(x):
#     return x * x
# print('如果输入的数字平方小于 50，程序将停止运行。')
# again = 1
# while again==1:
#     num = int(input('请输入一个数字：'))
#     print('运算结果为: %d' % (SQ(num)))
#     if SQ(num) >= 50:
#         again = 1
#     else:
#         again = 0 ;
print(1+2j) ;

# !/usr/bin/python
# -*- coding: UTF-8 -*-

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

n=1
print(type(n))
# <type 'int'>
n="runoob"
print(type(n))
# <type 'str'>











