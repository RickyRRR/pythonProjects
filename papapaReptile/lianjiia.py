#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 链家'
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
#请求页面
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url,headers=headers);
    if response.status_code==200:
        return response.text;
    return None;
    # print(response.text)
    pass



 #解析页面
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    # items = re.findall(pattern, html)

    doc = pq(html)


#数据写入文件
def write_to_json(content):
    with open('data/result.txt','a',encoding="utf-8") as f:
        #json.dumps(content)将dict格式的content转化成字符串（序列号），为了避免中文乱码 设置ensure_asili=false
        f.write(json.dumps(content, ensure_ascii=False, )+'\n')


#main
def main():
    url = 'https://hz.lianjia.com/ershoufang/103102337669.html'
    html = get_one_page(url)    #response.text
    print(html)
    # items = parse_one_page(html)
    # for item in items:
    #     print(item)
    #     # print(type(json.dumps(item)))
    #     # write_to_json(item)

if __name__ == '__main__':
    main()
