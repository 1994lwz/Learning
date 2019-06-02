#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#with open('student.txt', 'r') as f:
#    if f.read() == '':
#        print('hh')

from Student import student 

class student_system(object):
    
    __list = []

    def __init__(self):
        self.__list.append(student('01', 'Yang', 'male', 22))

    def menu(self):
        while True:
            print('please choice what you want to do?')
            print('1. add student')
            print('2. query student')
            print('3. delete student')
            print('4. modify student')
            print('5. show them all')
            print('6. exit')
            choice = input()
            if choice == '1':
                self.addstu()
            elif choice == '2':
                self.query_stu()
            elif choice == '3':
                self.delstu()
            elif choice == '4':
                self.modify_stu()
            elif choice == '5':
                self.showall()
            elif choice == '6':
                break
            else:
                print('Wrong number you choose, please input again')

    def showall(self):
        for student in self.__list:
            student.show_student()
               
    def addstu(self):
        idnum, name, sex, age = input('please input id, name, sex, age:').split()
        self.__list.append(student(idnum, name, sex, age))
        self.showall()

    def query_stu(self):
        idnum = input('Please input which id you want query:')
        Flag = False
        for index, student in enumerate(self.__list):
            if student.getID() == idnum:
                student.show_student()
                Flag = True
                return index

        if Flag == False:
            print('Don\'t have the student for this student system')
            return -1

    def delstu(self):
        index = self.query_stu()
        self.__list.pop(index)
        self.showall()

    def modify_stu(self):
        index = self.query_stu()
        if index < 0:
            print('Don\'t have the student for this student system')
        else:
            selection = input('which you want to choose to modify: (name/sex/age/course)')
            if selection == 'name':
                self.__list[index].change_name()
            elif selection == 'sex':
                self.__list[index].change_sex()
            elif selection == 'age':
                self.__list[index].change_age()
            elif selection == 'course':
                self.__list[index].change_source()
            else:
                print('wrong selection, break!')
        self.showall()
    

first = student_system()
first.menu()
