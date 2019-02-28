#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
import datetime
import json
import os

import pymongo

import schedule as schedule

import schedule

import yaml
from requests import HTTPError, Timeout

__author__ = 'ricky Xu'
import time,csv
from random import uniform,choice
import requests

from multiprocessing import Pool
from pyquery import PyQuery as pq
import pandas as pd
from fake_useragent import UserAgent
import logging
import logging.config


ua = UserAgent()
headers1 = {'User-Agent':'ua.ramdom'}

YAML_PATH = 'config.yaml'
Mongo_Url = 'localhost'
Mongo_Port = 27017
Mongo_DB = 'lianjia'
Mongo_TABLE = 'Lianjia hz'
client = pymongo.MongoClient(host=Mongo_Url, port=Mongo_Port)
db = client[Mongo_DB]

count = 0
# 一个我们将要爬取城市的列表
cities = ['bj', 'sh', 'nj', 'wh', 'cd', 'xa','hf']

def setup_logging(default_path='config.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


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



# def generate_allurl(user_in_nub, user_in_city):  # page1 page2的url
#      url = 'https://' + user_in_city + '.lianjia.com/ershoufang/pg{}/'
#      for url_next in range(1, int(user_in_nub)):
#          yield url.format(url_next)
#
#
# def get_allurl(generate_allurl):  # 分析url解析出每一页的详细url
#
#     get_url = requests.get(generate_allurl, headers=headers1, timeout=5)
#     if get_url.status_code == 200:
#         doc = pq(get_url.text)
#         detailItems = doc('.clear .img').items();
#         detailUrlList = []
#         for item in detailItems:
#             detailUrlList.append(item.attr("href"))
#
#         return detailUrlList


def open_url(detailUrl):  # 分析详细url获取所需信息

    #可以设置请求头 反爬虫
    try:
        res = requests.get(detailUrl,headers=headers1)
        if res.status_code == 200:
            info = {}
            doc = pq(res.text)
            info['title'] = doc('.main').text()  # soup.select('.main')[0].text    #标题
            info['totalPrice'] = doc('.price .total').text()  # soup.select('.total')[0].text + '万'    #总价
            info['squarePrice'] = doc('.price .unitPriceValue').text()  # soup.select('.unitPriceValue')[0].text  #每平方售价
            # info['参考总价'] = soup.select('.taxtext')[0].text
            info['buildTime'] = doc('.houseInfo .area .subInfo').text()  # soup.select('.subInfo')[2].text   建造时间
            info['buildAreaMeasure'] = doc('.houseInfo .area .mainInfo').text()   #面积
            info['communityName'] = doc('.aroundInfo  .communityName .info').text()  # 小区名称
            info['communityArea'] = ''
            for tempitem in doc('.aroundInfo  .areaName .info a').items():  # 所在区域
                info['communityArea'] += tempitem.text()

            doc('.houseRecord  .info').children().remove()
            info['lianjiaNo'] = doc('.houseRecord  .info').text()  #链家编号

            for temp in doc('.transaction ul li span').items():
                if temp.text() == '房协编码':
                    info['houseNo'] = temp.siblings().text()   #房协编号
                    break

            logging.info(info)
            return info
    except Exception:
        logging.error('OpenUrlError', exc_info=True)


#存储数据
def update_to_MongoDB(one_page):  # update储存到MongoDB
     if db[Mongo_TABLE].update({'lianjiaNo': one_page['lianjiaNo']}, {'$set': one_page}, True): #去重复  True的意思如果不存在插入，存在则更新

         logging.info('储存MongoDB 成功!')
         return True
     logging.info('储存MongoDB 失败!')
     return False
def pandas_to_xlsx(info):  # 储存到xlsx
     pd_look = pd.DataFrame(info,index = [0])
     pd_look.to_csv('链家二手房.csv',mode='a')

def writer_to_text(list):               #储存到text
    with open('链家二手房.text','a',encoding='utf-8')as f:
        f.write(json.dumps(list,ensure_ascii=False)+'\n')
        f.close()
def main(url):

    #解析详情页面内

    infoDict  = open_url(detailUrl=url)   #info字典类型
    infoDict['insertTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    infoDict['city'] = '杭州'
    #pandas_to_xlsx(infoDict)
    #writer_to_text(open_url(url))    #储存到text文件
    update_to_MongoDB(infoDict)   #储存到Mongodb

def getxiaoquList(city,region):
    url = 'https://' + city + '.lianjia.com/'+region+'/'
    return url
    # for url_next in range(1, int(user_in_nub)):
    #     yield url.format(url_next)
def getRegionsList(city):
    url = 'https://' + city + '.lianjia.com/xiaoqu'
    res = requests.get(url,headers=headers1);
    doc = pq(res.text)
    htmldiv = doc('.position')
    htmla = htmldiv('div[data-role="ershoufang"]').find('a')
    regionsUrlList = []
    for item in htmla.items():
        regionsUrlList.append(item.attr('href'))  #/xiaoqu/xihu/ 形式


    return regionsUrlList



def getPageUrlInRegion(baseUrl,region):
    url = baseUrl + region;
    res = requests.get(url,headers = headers1)
    if res.status_code==200 :
        doc = pq(res.text)
        if doc('div.resultDes span').text().strip() == '0':  #如果该行政区0套小区 返回None

            yield None
        else:
            dictStr = doc('.house-lst-page-box').attr('page-data')
            dictTemp = json.loads(dictStr)
            totalPage = dictTemp['totalPage']
            pageUrl = url+'pg{}/'
            for num in range(1,int(totalPage)):
                yield pageUrl.format(num)




def getXqInfoInPage(url,city):   #url=https://hz.lianjia.com/xiaoqu/xihu/pg1/
    res = requests.get(url,headers=headers1)
    if res.status_code == 200:
        doc = pq(res.text)
        htmla = doc('.listContent .info  .title a')
        htmlSpanCount = doc('.listContent .info  .title a')
        xqInfoUrl = 'https://'+city+'.lianjia.com/ershoufang/rs{}/'
        for item in htmla.items():
            yield   xqInfoUrl.format(item.text())  #返回搜索小区的链接

def getAllPageUrlInXq(baseUrl,xqUrlSearch):
    #url = baseUrl+'/ershoufang/rs'+xqName+'/'
    url = xqUrlSearch

    res = requests.get(url, headers=headers1)
    if res.status_code == 200:
        doc = pq(res.text)
        # temping = doc('div.resultDes span').text();

        if doc('div.resultDes span').text().strip() == '0':  #如果0套房子 返回None
            #print('小区0套房子在售')
            yield None
        # if len(doc('div.house-lst-page-box')) == 0:
        #     yield None
        else:
            temp = xqUrlSearch.split('/')[-2]
            xqName = temp[2:]
            #xqName = doc('div.agentCardSemInfoName a.agentCardResblockTitle').text()
            # print(len(doc('div.agentCardSemInfoName')))
            # print('小区名字：'+xqName)
            dictStr = doc('div.house-lst-page-box').attr('page-data')
            dictTemp = json.loads(dictStr)
            totalPage = dictTemp['totalPage']

            pageUrlInXq = baseUrl + '/ershoufang/pg{}rs'+xqName+'/'
            for num in range(1, int(totalPage)+1):
                yield pageUrlInXq.format(num)      #https://hz.lianjia.com/ershoufang/pg1rs金地自在城/



#返回小区某页中，所有跳转到具体房子的链接List
def getHouseInfoInPage(url):
    houseUrlList = []
    res = requests.get(url, headers=headers1)
    if res.status_code == 200:
        doc = pq(res.text)
        htmla = doc('a.noresultRecommend.img')
        for item in htmla.items():
            houseUrlList.append(item.attr('href'))
        return houseUrlList



def run():
    setup_logging(YAML_PATH)

def run():
    pass
    pool = Pool()  # 开启多线程
    regionPageCount = 0

    beginTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    beginTimeStamp = time.time();
    # user_in_city = input('输入爬取城市：')
    # user_in_nub = input('输入爬取页数：')
    city = 'hz'
    baseUrl = 'https://' + city + '.lianjia.com'
    regionsList = getRegionsList(city)
    # regionsList.remove('/xiaoqu/xihu/')

    logging.info(regionsList)
    print(regionsList)
    regionsList = ['/xiaoqu/linan/']

    for region in regionsList:  # region形式为/xiaoqu/xihu/  return

        # https://hz.lianjia.com/xiaoqu/xihu/pg1/
        pageUrlInRegion = getPageUrlInRegion(baseUrl=baseUrl, region=region)  # 行政区中小区列表的某一页   yield
        for pageUrl1 in pageUrlInRegion:
            try:
                if pageUrl1 == None:
                    logging.info('该行政区没有小区有在售二手房')
                    break
                regionPageCount += 1
                # print('行政区第'+str(regionPageCount)+'页')
                logging.info(str(region) + str(regionPageCount) + '页-  url:' + pageUrl1)

                # 行政区中的小区有很多页，某一页中所有指向小区的url组装成列表返回给xqUrlSearch 格式： https://hz.lianjia.com/ershoufang/rs金地自在城/
                xqUrlSearch = getXqInfoInPage(pageUrl1, city)  # yield  https://hz.lianjia.com/ershoufang/rs金地自在城/
                # xqSearchBaseUrl = baseUrl+'/ershoufang/rs'
                for xqurl in xqUrlSearch:
                    # print('开始爬取某个小区，url：'+xqurl)
                    logging.info('开始爬取某个小区，url：' + xqurl + '\n')

                    # 小区的在售房源有20页 1-20页，每页的url 返回给pageUrlInXq
                    pageUrlInXq = getAllPageUrlInXq(baseUrl=baseUrl,
                                                    xqUrlSearch=xqurl)  # https://hz.lianjia.com/ershoufang/pg1rs金地自在城/  yield
                    xqPageCount = 0

                    for pageUrl2 in pageUrlInXq:
                        if pageUrl2 == None:
                            # print('小区没有房子在售')
                            logging.info('小区没有房子在售')
                            break
                        xqPageCount += 1
                        # print('该小区第'+str(xqPageCount)+'页')
                        logging.info('该小区第' + str(xqPageCount) + '页  -url:' + pageUrl2)
                        # print(pageUrl2)
                        # 某个小区有很多房源，有很多页，某一页中所有指向所有房源的url组装成列表返回给houseUrlList
                        houseUrlList = getHouseInfoInPage(pageUrl2)  # return
                        # for tt in houseUrlList:
                        #     print(tt)
                        t = uniform(1, 3)
                        time.sleep(t)

                        pool.map(main, [url for url in houseUrlList])
            except Exception as e:
                logging.error('Error', exc_info=True)
            # finally:
            #     print('finally...')
            # except ConnectionError as e:
            #     print('遇到网络问题（如：DNS 查询失败、拒绝连接等')
            # except HTTPError as e:
            #     print('HTTP 请求返回了不成功的状态码{}'.format(e.code))
            # except Timeout as e:
            #     print('请求超时')

    # pool = Pool()  # 开启多线程
    # for pageUrl in generate_allurl('100', 'hz'):
    #     pageCount += 1
    #     print('第' + str(pageCount) + '页开始爬取。。。。。')
    #     t = uniform(1, 3)
    #     time.sleep(t)
    #     # 强制要求请求休息一下，我们这里用1，3之间的随机数
    #
    #
    #     try:
    #         pool.map(main, [url for url in get_allurl(pageUrl)])
    #     except ConnectionError as e:
    #         print('遇到网络问题（如：DNS 查询失败、拒绝连接等')
    #     except HTTPError as e:
    #         print('HTTP 请求返回了不成功的状态码{}'.format(e.code))
    #     except Timeout as e:
    #         print('请求超时')

    endTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    endTimeStamp = time.time();
    logging.info('爬取结束.....')
    logging.info('开始时间：' + beginTime + '   结束时间：' + endTime + '  -用时：' + str(endTimeStamp - beginTimeStamp))

<<<<<<< Updated upstream:lianjiaCrawl/lianjiaMain.py

if __name__ == '__main__':
    runRightnow = input('是否立即执行，y/n')
    if runRightnow == 'y':
        run()
    else:
        schedule.every().saturday.at('9:00').do(run)
        while True:
            schedule.run_pending()
            time.sleep(1)

=======
if __name__ == '__main__':
    schedule.every().saturday.at('9:00').do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)

    # pool = Pool()  # 开启多线程
    # regionPageCount = 0
    #
    # beginTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    # beginTimeStamp = time.time();
    # # user_in_city = input('输入爬取城市：')
    # # user_in_nub = input('输入爬取页数：')
    # city = 'hz'
    # baseUrl = 'https://' + city + '.lianjia.com'
    # regionsList = getRegionsList(city)
    # #regionsList.remove('/xiaoqu/xihu/')
    #
    # logging.info(regionsList)
    # regionsList = ['/xiaoqu/xiaoshan/']
    #
    # for region in regionsList:   #region形式为/xiaoqu/xihu/  return
    #
    #     #https://hz.lianjia.com/xiaoqu/xihu/pg1/
    #     pageUrlInRegion = getPageUrlInRegion(baseUrl= baseUrl,region=region) #行政区中小区列表的某一页   yield
    #     for pageUrl1 in pageUrlInRegion:
    #         try:
    #             regionPageCount += 1
    #             # print('行政区第'+str(regionPageCount)+'页')
    #             logging.info(str(region)+str(regionPageCount)+'页-  url:'+pageUrl1)
    #
    #             #行政区中的小区有很多页，某一页中所有指向小区的url组装成列表返回给xqUrlSearch 格式： https://hz.lianjia.com/ershoufang/rs金地自在城/
    #             xqUrlSearch = getXqInfoInPage(pageUrl1,city)    #yield  https://hz.lianjia.com/ershoufang/rs金地自在城/
    #             #xqSearchBaseUrl = baseUrl+'/ershoufang/rs'
    #             for xqurl in xqUrlSearch:
    #                 # print('开始爬取某个小区，url：'+xqurl)
    #                 logging.info('开始爬取某个小区，url：'+xqurl+'\n' )
    #
    #                 # 小区的在售房源有20页 1-20页，每页的url 返回给pageUrlInXq
    #                 pageUrlInXq = getAllPageUrlInXq(baseUrl=baseUrl,xqUrlSearch=xqurl)    #https://hz.lianjia.com/ershoufang/pg1rs金地自在城/  yield
    #                 xqPageCount = 0
    #
    #                 for pageUrl2 in pageUrlInXq:
    #                     if pageUrl2 == None:
    #                         # print('小区没有房子在售')
    #                         logging.info('小区没有房子在售')
    #                         break
    #                     xqPageCount += 1
    #                     # print('该小区第'+str(xqPageCount)+'页')
    #                     logging.info('该小区第'+str(xqPageCount)+'页  -url:'+pageUrl2)
    #                     # print(pageUrl2)
    #                     # 某个小区有很多房源，有很多页，某一页中所有指向所有房源的url组装成列表返回给houseUrlList
    #                     houseUrlList = getHouseInfoInPage(pageUrl2)    #return
    #                     # for tt in houseUrlList:
    #                     #     print(tt)
    #                     t = uniform(1, 3)
    #                     time.sleep(t)
    #
    #                     pool.map(main, [url for url in houseUrlList])
    #         except Exception as e:
    #             logging.error('Error', exc_info=True)
    #         # finally:
    #         #     print('finally...')
    #         # except ConnectionError as e:
    #         #     print('遇到网络问题（如：DNS 查询失败、拒绝连接等')
    #         # except HTTPError as e:
    #         #     print('HTTP 请求返回了不成功的状态码{}'.format(e.code))
    #         # except Timeout as e:
    #         #     print('请求超时')
    #
    # endTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    # endTimeStamp = time.time();
    # logging.info('爬取结束.....' )
    # logging.info('开始时间：'+beginTime + '   结束时间：'+endTime + '  -用时：' + str(endTimeStamp - beginTimeStamp))
>>>>>>> Stashed changes:lianjiaCrawl/lianjiaMainc.py


