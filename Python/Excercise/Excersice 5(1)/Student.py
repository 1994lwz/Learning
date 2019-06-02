#!python3.6
# -*- coding: utf-8 -*-

class student():

	def __init__(self, idNumber, name, sex, age):

		self.__idNumber = idNumber
		self.__name = name
		self.__sex = sex
		self.__age = age
		self.__course = {}

	def getID(self):

		return self.__idNumber

	def addCourse(self):

		courseName, courseGrade = input('please input the course_name and course_grade: ').split()
		self.__course[courseName] = courseGrade

	def modifyCourse(self):

		courseName = input('please input the courseName you want to change: ')
		
		if courseName in self.__course:
			self.__course.pop(courseName)
			self.addCourse()
		else:
			print('course not found!')
			print('do you wanna add the course?(y/n)')
			choice = input()

			if choice == 'y':
				self.addCourse()

	# def deleteCourse(self):

	# 	courseName = input('please input the course_name you wang to delete: ')
	# 	self.__course.pop('courseName')

	def modifyName(self):

		name = input('please input the name you want to change to: ')
		self.__name = name

	def modifySex(self):

		sex = input('please input the sex you want to change to: ')
		self.__sex = sex

	def modifyAge(self):

		age = input('please input the age you want to change to: ')
		self.__age = age


	def showStudent(self):
		print(self.__idNumber,self.__name,self.__sex,self.__age)
		print('--------------------------------')
		for key, value in self.__course.items():
			print(key, value)

