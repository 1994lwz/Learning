#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#name = input("Please input you name:")
#print("Are you name is:", name)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

##############汉诺塔算法##################
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
num = input('Please in input the number of the plates:')
print("The order of movement is as follows:\n")
move(int(num), 'A', 'B', 'C')

##########杨辉三角via生成器##################
def triangles():
    list = [1]
    while True:
        yield list
        list = [list[x] + list[x + 1] for x in range(len(list) - 1)]
        list.insert(0, 1)
        list.append(1)
        
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break