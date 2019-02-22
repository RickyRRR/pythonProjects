#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '

__author__ = 'ricky Xu'
import time,csv
from random import uniform,choice
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pyquery import PyQuery as pq
# 一个我们将要爬取城市的列表
cities = ['bj', 'sh', 'nj', 'wh', 'cd', 'xa','hf']

def get_city():
    global cities
    try:
        city = choice(cities)
        cities.remove(city)
        # 随机选取一个城市进行爬取，然后再列表中删除这个城市
        print(cities)
    except IndexError:
        return None
    # 当没有城市了，就返回一个None
    return city



def generate_allurl(user_in_nub, user_in_city):  # page1 page2的url
     url = 'https://' + user_in_city + '.lianjia.com/ershoufang/pg{}/'
     for url_next in range(1, int(user_in_nub)):
         yield url.format(url_next)

def get_allurl(generate_allurl):  # 分析url解析出每一页的详细url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    get_url = requests.get(generate_allurl, headers=headers)
    if get_url.status_code == 200:
        doc = pq(get_url.text)
        detailItems = doc('.clear .img').items();
        detailUrlList = []
        for item in detailItems:
            detailUrlList.append(item.attr("href"))

        return detailUrlList

def open_url(detailUrl,headers):  # 分析详细url获取所需信息
    #可以设置请求头 反爬虫
    try:
        res = requests.get(detailUrl,headers=headers)
        if res.status_code == 200:
            info = {}
            doc = pq(res.text)
            info['标题'] = doc('.main').text()  # soup.select('.main')[0].text
            info['总价'] = doc('.price .total').text()  # soup.select('.total')[0].text + '万'
            info['每平方售价'] = doc('.price .unitPriceValue').text()  # soup.select('.unitPriceValue')[0].text
            # info['参考总价'] = soup.select('.taxtext')[0].text
            info['建造时间'] = doc('.houseInfo .area .subInfo').text()  # soup.select('.subInfo')[2].text
            info['小区名称'] = doc('.aroundInfo  .communityName .info').text()  # soup.select('.info')[0].text
            info['所在区域'] = ''
            for tempitem in doc('.aroundInfo  .areaName .info a').items():  # soup.select('.info a')[0].text + ':' + soup.select('.info a')[1].text
                info['所在区域'] += tempitem.text()
            info['链家编号'] = doc('.houseRecord  .info').text()

            for temp in doc('.transaction  .info .li .span').items():
                if temp.text() == '房协编码':
                    info['房协编号'] = temp.siblings().text()

            print(info)
            return info
    except AttributeError:
        print('我发现了一个错误')
    except UnicodeEncodeError:
        print('有一个编码错误')
def main(url):
    #解析详情页面内
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    info  = open_url(detailUrl=url,headers=headers)   #info字典类型
     #writer_to_text(open_url(url))    #储存到text文件
     # update_to_MongoDB(list)   #储存到Mongodb


if __name__ == '__main__':
    # user_in_city = input('输入爬取城市：')
    # user_in_nub = input('输入爬取页数：')

    # Mongo_Url = 'localhost'
    # Mongo_DB = 'Lianjia'
    # Mongo_TABLE = 'Lianjia' + '\n' + str('zs')
    # client = pymongo.MongoClient(Mongo_Url)
    # db = client[Mongo_DB]
    pool = Pool()  #开启多线程
    for pageUrl in generate_allurl('50', 'hz'):
        t = uniform(1, 3)
        time.sleep(t)
        # 强制要求请求休息一下，我们这里用1，3之间的随机数
        pool.map(main, [url for url in get_allurl(pageUrl)])
