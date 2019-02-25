#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import datetime
# time.time()  时间戳
now_time = datetime.datetime.now()
a = now_time.strftime('%Y-%m-%d %H:%M:%S')
print(now_time)
print('a'+a)