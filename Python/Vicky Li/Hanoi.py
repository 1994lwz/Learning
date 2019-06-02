#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

while True:
    num = input('Please in input the number of the plates:')
    if num.isdigit():
        break
    else:
        print('ValueError: the input is not a int type, Please re-enter.')

print("The order of movement is as follows:")
move(int(num), 'A', 'B', 'C')