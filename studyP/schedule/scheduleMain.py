#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import datetime

import schedule
import time


def job1():
    print("I'm working for job1")
    # time.sleep(2)
    print("job1:", datetime.datetime.now())


def job2():
    print("I'm working for job2")
    # time.sleep(2)
    print("job2:", datetime.datetime.now())


def job():
    print("I'm working...")


def run():
    varName=input('是否立即执行y/n?')
    if varName == 'y':
        print('right now')
        job2()
    else:
        schedule.every(5).seconds.do(job1)
        schedule.every(10).seconds.do(job2)
        while True:
            schedule.run_pending()
            time.sleep(1)

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

#

if __name__ == '__main__':
    run()
    pass