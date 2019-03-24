#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import re

__author__ = 'ricky Xu'

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
pp = '''
<p><i class="i_01"></i>3室2厅1卫·86.57  平米  ·  南北  ·  低楼层/27层  ·  简装</p>
'''
dd = '''
<div class="Tem-row">
                                            <span class="fc-gray">
                                                 3室2厅&nbsp;&nbsp;119.0方
                                            </span>
                                        </div>
'''
html = etree.HTML(dd)
# result = etree.tostring(html)
p = html.xpath("//div/span/text()")
result = p[0].split()
print(result)
totalCount = '12.0abc'
totalCount = re.sub("\D", "", totalCount)
print(totalCount)
# print(result[0])