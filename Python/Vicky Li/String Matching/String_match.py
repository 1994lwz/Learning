#!/usr/bin/env python3
# -*- coding: utf-8 -*-

deststr = '水'
f = open('sample.txt', 'r', errors = 'ignore')
sum = 0
for index, line in enumerate(f.readlines()):
    pos = line.find(deststr)
    print(pos)
    while pos != -1:
        sum += 1
        print(index, pos)
        pos = line.find(deststr, pos+1, -1)
f.close()
print('number of 水 is %s' %sum)
