#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
#dumps()方法返回一个str，内容就是标准的JSON。
#dump()方法可以直接把JSON写入一个file-like Object
print('JSON Data is a dict:', data)
reborn = json.loads(data)
#loads()方法把JSON的字符串反序列化
#load()方法从file-like Object中读取字符串并反序列化：
print(reborn)


class Student(object):
    """Student class"""
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %d, %d)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，需要传入转换函数
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
#可选参数object_hook可将序列话的JSON对象转换成相应的数据类型，需要传入转换函数
print(rebuild)

obj = dict(name='阿中', age=20)
print(json.dumps(obj, ensure_ascii=False))

# 用json进行序列化时,可选参数ensure_ascii设置成False可以使程序输出中文
# ensure_ascii缺省值为True，默认把中文转换成ASCII编码
