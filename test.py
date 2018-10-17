# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:43:20 2018

@author: ybhuo
"""
import fractions as f
print(f.Fraction("1/3")+5)
print(f.Fraction(1.25))
print(f.Fraction("1/8")*-2/9+f.Fraction(7/8))
# ====================== 分子分母 ====================
# 获取分子分母
m=f.Fraction("11/6").numerator
n=f.Fraction("11/56").denominator
print(m,n)

# ===================== 字符串切片 ======================
print("切片")
d="0123456789"
print(d[::2])
print(d[1:4])
print(d[1::2])
print(d[-2::-2])
print(d[::-1])

# ===================== 字符串替换 ======================
str1="You need Python"
print(str1[0])
print(str1[-1])
print(len(str1))
# this is important
print(str1.replace("You","I"))

print(str1.upper())
print(str1.lower())
lst1=str1.split(' ')
print(lst1)