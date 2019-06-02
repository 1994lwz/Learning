#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProductAPP(object):
    __slots__ = ('__Company', '__Type', '__Price', '__Color')
    def __init__(self, Company, Type, Price, Color):
        self.__Company = Company
        self.__Type = Type
        self.__Price = Price
        self.__Color = Color

    def get_Company(self):
        return self.__Company

    def get_Type(self):
        return self.__Type

    def get_Price(self):
        return self.__Price

    def get_Color(self):
        return self.__Color

    def set_Company(self, Company):
        self.__Company = Company

    def set_Type(self, Type):
        self.__Type = Type

    def set_Price(self, Price):
        self.__Price = Price

    def set_Color(self, Color):
        self.__Color = Color

list = []
p1 = ProductAPP('Apple', 'Mobile', 'High', 'White')
list.append(p1)

p2 = ProductAPP('Samsung', 'Mobile', 'High', 'White')
list.append(p2)

p3 = ProductAPP('LG', 'Mobile', 'High', 'Gray')
list.append(p3)

p4 = ProductAPP('HTC', 'Mobile', 'High', 'Gray')
list.append(p4)

p5 = ProductAPP('Xiaomi', 'Mobile', 'Low', 'Black')
list.append(p5)

p6 = ProductAPP('Huawei', 'Mobile', 'Low', 'Black')
list.append(p6)

p7 = ProductAPP('ZTE', 'Mobile', 'Low', 'Red')
list.append(p7)

p8 = ProductAPP('Lenovo', 'Mobile', 'Low', 'Red')
list.append(p8)

#print(list)
In = input('请输入你想查询的条件及其值，用空格分隔：').split()
if In[0].title() == 'Company':
    i = 0
    try:
        for x in list:
            if x.get_Company() == In[1].title():
                print('Company =', x.get_Company(), ', Type =', x.get_Type(), ', Prince =', x.get_Price(), ', Color =', x.get_Color())
                i += 1
        
        if i == 0:
            print('没有符合该条件值的产品')
    except:
        print('IndexError: 没有输入该条件的值')
elif In[0].title() == 'Type':
    i = 0
    try:
        for x in list:
            if x.get_Type() == In[1].title():
                print('Company =', x.get_Company(), ', Type =', x.get_Type(), ', Prince =', x.get_Price(), ', Color =', x.get_Color())
                i += 1
        
        if i == 0:
            print('没有符合该条件值的产品')
    except:
        print('IndexError: 没有输入该条件的值')
elif In[0].title() == 'Price':
    i = 0
    try:
        for x in list:
            if x.get_Price() == In[1].title():
                print('Company =', x.get_Company(), ', Type =', x.get_Type(), ', Prince =', x.get_Price(), ', Color =', x.get_Color())
                i += 1
        
        if i == 0:
            print('没有符合该条件值的产品')
    except:
        print('IndexError: 没有输入该条件的值')
elif In[0].title() == 'Color':
    i = 0
    try:
        for x in list:
            if x.get_Color() == In[1].title():
                print('Company =', x.get_Company(), ', Type =', x.get_Type(), ', Prince =', x.get_Price(), ', Color =', x.get_Color())
                i += 1
        
        if i == 0:
            print('没有符合该条件值的产品')
    except:
        print('IndexError: 没有输入该条件的值')
else:
    print('输入的查询条件有误')

