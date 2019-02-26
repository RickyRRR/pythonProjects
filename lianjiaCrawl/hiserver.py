#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import time

import schedule


def hi():
    print('hiserver')


if __name__ == '__main__':
    schedule.every(3).minutes.do(hi)
    while True:
        schedule.run_pending()
        time.sleep(1)
