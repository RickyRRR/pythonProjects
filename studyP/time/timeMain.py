#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import datetime
# time.time()  时间戳
import math
import time

now_time = datetime.datetime.now()
a = now_time.strftime('%Y-%m-%d %H:%M:%S')
b = now_time.strftime('%Y%m%d')


def testTime():
    info = {}
    info["name"] = 'ricky'
    info["time" + b] = str(now_time.strftime('%Y-%m-%d %H:%M:%S'))
    print(info)


# 日期时间字符串
st = "2017-11-23 16:10:10"
# 当前日期时间
dt = datetime.datetime.now()
# 当前时间戳
sp = time.time()

# 1.把datetime转成字符串
def datetime_toString(dt):
    print("1.把datetime转成字符串: ", dt.strftime("%Y-%m-%d %H:%M:%S"))


# 2.把字符串转成datetime
def string_toDatetime(st):
    datedt = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
    print("2.把字符串转成datetime: ", datedt)
    print(type(datedt))


# 3.把字符串转成时间戳形式
def string_toTimestamp(st):
    print("3.把字符串转成时间戳形式:", time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S")))


# 4.把时间戳转成字符串形式
def timestamp_toString(sp):
    print("4.把时间戳转成字符串形式: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sp)))


# 5.把datetime类型转外时间戳形式
def datetime_toTimestamp(dt):
    print("5.把datetime类型转外时间戳形式:", time.mktime(dt.timetuple()))

if __name__ == '__main__':
    # testTime()
    # string_toDatetime('2019-02-28 16:24:19')
    # starttime =
    finishtime = datetime.datetime(2019, 3, 22, 14, 40, 27, 84437).strftime('"%Y-%m-%d %H:%M:%S"')
    print(type(dt))
    print(dt)

    num = 120/30
    print(math.ceil(num))


