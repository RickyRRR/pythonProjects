#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 爬虫主程序 '
import json

import requests
from requests import RequestException
import re
__author__ = 'ricky Xu'
from urllib import  request


#help(request)
page = request.urlopen('http://tieba.baidu.com/p/1753935195')  # 打开网页

htmlcode = page.read().decode('utf-8',errors='ignore')
#print(htmlcode)
#print(page.getcode())
#print(page.read().decode('utf-8'))
with open('pageCode.txt','w') as pageFile:
    pageFile.write(htmlcode);

# pageFile = open('pageCode.txt','w') ;
# pageFile.write(htmlcode);

def write_to_file(content):
    with open('xiaoxi.txt', 'a', encoding='utf-8')as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False))

def get_page(url):
    try:
        response = requests.get(url);
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield{
            'title': item[0],
            'score': item[1],
            'image': item[2],
        }

def main():
    url = "https://movie.douban.com/cinema/nowplaying/beijing/"
    html = get_page(url)
    # print(html)
    for item in parse_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    main();

