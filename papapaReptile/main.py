#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(response.read().decode('utf-8'))