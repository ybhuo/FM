# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:31:06 2018
Range.py,this script includs the instanses for range()
Point list:
    1. 一般用法foreeach中
    2. 非pythonic的用法构造索引
    3. 三种方式，三个参数
    4. 注意
        a.step不能为0
        b.索引与切片不同（range的惰性）
        c.浮点数的（list）numpy.arrange与（list）numpy.linspace(start,stop,numberOf)
    5. 主要用途
        a.执行for循环的主体特征次数
        b.创建比列表或元组更有效的整数迭代
@author: ybhuo
"""

captains = ["Janeway","Pivard","Sisko"]
# for 基本用法，foreach方式
for captain in captains:
    print(captain)
    

# 按列表循环与格式输出
numbers_divisible_by_three = [3,6,9,12,15]
for num in numbers_divisible_by_three:
    quotient = num/3
    print("{} divided by 3 is {}.".format(num,int(quotient)))

print("##############################")
# range（start，end，gap）产生从start到end的间隔为gap的列表
for i in range(3,16,3):
    quotient = i/3
    print("{} divided by 3 is {}.".format(num,int(quotient)))
    
# 不是Pythonic（这很Python）
# range()非常适合创建数字的迭代，
# 但是当您需要迭代可以与in运算符循环的数据时，
# 它不是最佳选择。
for i in range(len(captains)):
    print(captains[i])
# python缩进是严格的，多个空格会导致编译错误  
print("range的三种用法您可以通过三种方式调用range()：\n \
       1.range(stop) 有一个参数。默认从0开始，左闭右开的\n\
       2.range(start, stop) 有两个参数。\n\
       3.range(start, stop, step) 有三个参数。step不能为0")

# range进行递增
print('--------- 递增 ---------')
for i in range(3,100,25):
    print(i)
# range递减
print('--------- 递减 ---------')
for i in range(10,-6,-2):
    print(i)
print("注意事项")
print("1. 倒序#注意range是个类，直接 输出会按类显示")
print("    ",list(range(10,1,-1)))
print("    ",list(reversed(range(10))))
print("    ",list(reversed("abcdefg")))
print ("   ",range(5))
print("2. 索引会返回值")
print(range(3)[1])
print("   但切片只会返回range（惰性的）")
print(range(3)[1:2])
print("3. 不能使用浮点数，除非使用Numpy,np.arange(start,end,gap)或np.linspace(start,end,num)返回列表")
import numpy as np
ar=np.arange(0.3,1.6,.3)
lsp=np.linspace(0.1,1.6,3)
print("   ",ar)
print("   ",lsp)
print("range 主要用于两个目的：\n \
      1. 执行for循环的主体特征次数\n \
      2. 创建比列表或元组更有效的整数迭代")