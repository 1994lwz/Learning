#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Bubble_Sort(list_old):
	list = list_old[ : ]
	for i in range(0, len(list)):
		for j in range(i + 1, len(list)):
			if(list[i] > list[j]):
				list[i], list[j] = list[j], list[i]
	return list

def Shell_Sort(list_old):
	list = list_old[ : ]
	group = len(list) // 2
	while(group > 0):
		for i in range(0, group):
			j = i + group
			while j < len(list):
				k = j - group
				key = list[j]
				while k >= 0:
					if list[k] > key:
						list[k + group] = list[k]
						list[k] = key
					k -= group
				j += group
		group = group // 2
	return list
	
def adjust_heap(list, i, lenth):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < lenth // 2:
        if lchild < lenth and list[lchild] > list[max]:
            max = lchild
        if rchild < lenth and list[rchild] > list[max]:
            max = rchild
        if max != i:
            list[max], list[i] = list[i], list[max]
            adjust_heap(list, max, lenth)
 
def build_heap(list, lenth):
    for i in range(0, (lenth//2))[::-1]:
        adjust_heap(list, i, lenth)
	
def Heap_Sort(list_old):
	list = list_old[ : ]
	build_heap(list, len(list))
	for i in range(0, len(list))[::-1]:
		list[0], list[i] = list[i], list[0]
		adjust_heap(list, 0, i)
	return list
	
def Quick_Sort(list, left, right):
	#list = list_old[ : ]
	if left >= right:
		return list
	key = list[left]
	low = left
	high = right
	while left < right:
		while left < right and list[right] >= key:
			right -= 1
		list[left] = list[right]
		while left < right and list[left] <= key:
			left += 1
		list[right] = list[left]
	list[left] = key
	Quick_Sort(list, low, left)
	Quick_Sort(list, left + 1, high)
	return list

while True:	
    i = 0
    L = input('Please input the number list and separated by spaces:').split()
    while i < len(L):
        try:
            L[i] = float(L[i])
        except:
            print('ValueError: the input is not a int type, Please re-enter.')
            break
        i += 1
    if i == len(L):
        break
print("The result of Bubble_Sort:", Bubble_Sort(L))
print("The result of Shell_Sort:", Shell_Sort(L))
print("The result of Heap_Sort:", Heap_Sort(L))
L_new = L[ : ]
print("The result of Quick_Sort:", Quick_Sort(L_new, 0, len(L_new) - 1))
