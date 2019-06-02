#!python3.6
# -*- coding: utf-8 -*-
from Student import student

class MIS():

	__list = []

	def __init__(self):
		
		self.__list.append(student('001', 'Zhang', 'male', 19))

	def menu(self):

		while True:
			print('please choice what you want to do?')
			print('1. add student')
			print('2. query student')
			print('3. delete student')
			print('4. modify student')
			print('5. show them all')
			choice = input()

			if choice == '1':
				self.addStudent()
			elif choice == '2':
				self.queryStudent()
			elif choice == '3':
				self.deleteStudent()
			elif choice == '4':
				self.modify()
			elif choice == '5':
				self.showAll()
			else:
				print('wrong number you choose!!')

	def showAll(self):
		for student in self.__list:
			student.showStudent()

	def addStudent(self):
		
		idNumber, name, sex, age = input('please input id, name, sex, age:').split()
		self.__list.append(student(idNumber, name, sex, age))

		self.showAll()

	def queryStudent(self):
		
		idNumber = input('please input the id: ')
		found = False

		for index, student in enumerate(self.__list):
			if student.getID() == idNumber:
				student.showStudent()
				found = True
				return index
			
		if found == False:
			print('don\'t have the student for this id')
			return -1
	
	def deleteStudent(self):
		
		index = self.queryStudent()
		self.__list.pop(index)

	def modify(self):

		index = self.queryStudent()

		if index < 0:
			print('back to menu')
		else:
			selection = input('which you want to choose to modify: (name/sex/age/course)')

			if selection == 'name':
				self.__list[index].modifyName()
			elif selection == 'sex':
				self.__list[index].modifySex()
			elif selection == 'age':
				self.__list[index].modifyAge()
			elif selection == 'course':
				self.__list[index].modifyCourse()
			else:
				print('wrong selection, break!')
				


a = MIS()
a.menu()