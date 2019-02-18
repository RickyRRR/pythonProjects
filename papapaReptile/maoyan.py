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
#请求页面
def get_one_page(url):
    response = requests.get(url);
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
    all = doc('dd')
    for item in all.items():
        index = item('i.board-index').text();

        # print('dddd'+str(test))
        image = item('a img.board-img').attr('data-src');
        title = item('div p.name ').text();
        actor = item('div p.star ').text();
        time = item('div.movie-item-info p.releasetime ').text();
        score = item('div.score-num p.score' ).text()
        # bb = item('div.score-num p.score .integer');
        # score1 = item('div.movie-item-info p.score .fraction').text();

        yield {
            'index': index,
            'image': image,
            'title': title.strip(),
            'actor': actor.strip()[3:] if len(actor) > 3 else '',
            'time': time.strip()[5:] if len(time) > 5 else '',
            'score':score
        }
    # for item in items:
    #     yield {
    #         'index': item[0],
    #         'image': item[1],
    #         'title': item[2].strip(),
    #         'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
    #         'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
    #         'score': item[5].strip() + item[6].strip()
    #     }
        # print(items)


#数据写入文件
def write_to_json(content):
    with open('data/result.txt','a',encoding="utf-8") as f:
        #json.dumps(content)将dict格式的content转化成字符串（序列号），为了避免中文乱码 设置ensure_asili=false
        f.write(json.dumps(content, ensure_ascii=False, )+'\n')


#main
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)    #response.text
    items = parse_one_page(html)
    for item in items:
        print(item)
        # print(type(json.dumps(item)))
        # write_to_json(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10);
