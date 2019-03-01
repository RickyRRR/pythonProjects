#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import time

import schedule

count = 0
def hi():
    print('hiserver')

def forTest():

    list = [1,2,3]
    for i in list:
        print(i)
        if i == 3:
            list.append(4)
def globalVar():
    global count
    if True:
        count += 1
def run():
    print(count)
if __name__ == '__main__':
    # schedule.every(3).minutes.do(hi)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    a = [1,2]
    for i in range(3):
        globalVar()
    run()