#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 正则爬取猫眼电影 top100'
__author__ = 'ricky Xu'

# 参考：Response对象的属性
# r.status_code
# http请求的返回状态，200
# 表示连接成功，404
# 表示连接失败
#
# r.text
# http响应内容的字符串形式，url对应的页面内容
#
# r.encoding
# 从HTTP
# header中猜测的响应内容编码方式
#
# r.apparent_encoding
# 从内容分析出的响应内容的编码方式（备选编码方式）
#
# r.content
# HTTP响应内容的二进制形式
#
# r.headers
# http响应内容的头部内容
import  requests;
import  re;
import json
from pyquery import PyQuery as pq

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H326249Y5D71GEYD"
proxyPass = "FFD8D67F19655B38"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}


#请求页面
def get_one_page(url):
    for i in range(16):
        r = requests.get('https://hz.5i5j.com/ershoufang/')
        print(r.text)
        print(r.status_code)
    # r = requests.get('http://p.ashtwo.cn')
    # print(r.text)
    # doc = pq(r.text)
    # aa = doc.find('p').text()
    # print(aa)


    pass



 #解析页面



if __name__ == '__main__':
    get_one_page('')
