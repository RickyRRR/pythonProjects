#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'

# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.read().decode('utf-8'))



# from urllib import request, error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)
# #
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

#
# import requests
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(r.text)
#
# print(r.json())
#
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)





# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# print(type((html)))
# result = etree.tostring(html)
# print(type(result))
# print(result.decode('utf-8'))



#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)



html = '''
<div id="container">
    <ul class="list">
         <li class="item-0" title="cctitle">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
# print(type(doc))
subdoc = doc('#container .list li')
test=  subdoc('[title="cctitle"]')
print(doc('#container .list li'))