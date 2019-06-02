#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

#lock = threading.Lock()

def minute():
    j = 5
    k = 60
    for i in range(4):
        #lock.acquire()
        #try:
        j -= 1
        time.sleep(60)
        print('还有%s分钟' %j)
        #finally:
            #lock.release()
    for i in range(60):
        #lock.acquire()
        #try:
        k -= 1
        time.sleep(1)
        print('还有%s秒' %k)
        #finally:
            #lock.release()

def second():
    time.sleep(60*4)
    k = 60
    for i in range(60):
        #lock.acquire()
        #try:
        k -= 1
        time.sleep(1)
        print('还有%s秒' %k)
        #finally:
            #lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target = minute)
    #t2 = threading.Thread(target = second)
    print('还有5分钟')
    t1.start()
    #t2.start()
    t1.join()
    #t2.join()
    print('倒计时结束')
    
    
