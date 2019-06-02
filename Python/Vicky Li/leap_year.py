#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def leap_year(year):
	if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
		print('Congratulations: this year is a leap year.')
		return True
	else:
		print('Sorry: this year is not a leap year, please input again')
		return False

while True:		
	a = input('Please input a year:')
	if leap_year(int(a)):
		break