#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '

def foo(s):

    return 10 / int(s)


def bar(s):

    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


if __name__ == '__main__':
    main()