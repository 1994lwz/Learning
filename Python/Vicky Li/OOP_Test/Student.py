#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class student(object):

    def __init__(self, idnum, name, sex, age):
        self.__idnum = idnum
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__source = {}

    def getID(self):
        return self.__idnum
    
    def change_name(self):
        new = input('Please input the student\'s name: ')
        self.__name = new

    def change_sex(self):
        new = input('Please input the student\'s sex: ')
        self.__sex = new

    def change_age(self):
        new = input('Please input the student\'s age: ')
        self.__age = new

    def add_source(self):
        source_name, source_value = input('Please input the student\'s source_name and grade:').split()
        self.__source[source_name] = source_value

    def change_source(self):
        source_name, source_value = input('Please input the source_name and the grade which you want change:').split()
        if source_name in self.__source:
            self.__source[source_name] = source_value
        else:
            print('Don\'t have this source, did you want add one?(y/n)')
            choice = input()
            if choice == 'y':
                self.add_source()

    def show_student(self):
        print('idnumber = %s, name = %s, sex = %s, age = %s' %(self.__idnum, self.__name, self.__sex, self.__age))
        print('--------------------------------')
        for key, value in self.__source.items():
            print('%s = %s' %(key, value))
        print('--------------------------------')
