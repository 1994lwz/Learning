#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    x1 = (-b + (math.sqrt(b * b - 4 * a * c))) / (2 * a)
    x2 = (-b - (math.sqrt(b * b - 4 * a * c))) / (2 * a)
    
    return x1, x2

print('quadratic(2, 3, 2) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print("测试失败")
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")

def product(x, y = 1, *args):
    m = x * y
    #print(args)
    for n in args:
        m = m * n
    return m
    
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')