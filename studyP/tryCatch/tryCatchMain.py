#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import json


def foo(s):

    return 10 / int(s)


def bar(s):

    return foo(s) * 2

def jsonDict():
    dictStr = None
    dictTemp = json.loads(dictStr)
def main():

    for i in range(3):
        print(i)
        try:
            # bar('0')
            jsonDict()

        except Exception as e:
            print('Error..:', e)
        finally:
            print('finally...')


if __name__ == '__main__':
    main()