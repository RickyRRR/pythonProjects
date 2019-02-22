#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 爬取杭州豆瓣信息 '
import io
from PIL import Image
import requests
from pyquery import PyQuery as pq
import urllib.request
__author__ = 'ricky Xu'
import sys
import logging
from io import StringIO
import os

def savaImg(imgUrlList):
    """
    保存图片到本地
    :param imgList:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    #判断目录是否存在
    isExists = os.path.exists('./img')
    #如果不存在创建
    if not isExists:
        os.makedirs('./img')
    for t in imgUrlList:
        fileName = t[-14:-4]
        filePath = './img/'+fileName+'.jpg'
        urllib.request.urlretrieve(t, filename=filePath)
        # res = requests.get(t,headers=headers)
        # byte_stream = io.BytesIO(res.content)  # 把请求到的数据转换为Bytes字节流
        # roiImg = Image.open(byte_stream)  # Image打开Byte字节流数据
        #
        # imgByteArr = io.BytesIO()  # 创建一个空的Bytes对象
        #
        # roiImg.save(imgByteArr, format='PNG')  # PNG就是图片格式，我试过换成JPG/jpg都不行
        #
        # imgByteArr = imgByteArr.getvalue()  # 这个就是保存的图片字节流
        # # 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
        # fileName = t[-14:-4]
        # filePath = './img/'+fileName+'.png'
        # with open(filePath, "wb") as f:
        #     f.write(imgByteArr)
def getImgLink(urls):
    """
    获取帖子里所有图片的链接
    :param url:
    :return:
    """
    headers = {
        # 'Connection': 'keep-alive',
        # 'Upgrade-Insecure-Requests': '1',
        # 'Referer': 'https://www.douban.com/group/haixiuzu/discussion?start=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    imgUrlList = []
    for url in urls:
        response = requests.get(url,headers=headers)
        html = response.text;
        doc = pq(html)
        content = doc.find('div.topic-doc')
        #获取图片链接

        divimgList = content('div.topic-content').find('div.image-wrapper').items()
        for divimg in divimgList:
            imgUrlList.append(divimg('img').attr('src'))

    savaImg(imgUrlList = imgUrlList)



def getPageLink(url,begin,end):
    """
    获取小组主页全部帖子链接
    :param url:
    :return:
    """
    #构建所有URL
    urlList = []
    #构建所有需要获取的链接
    for page in range(begin,end+1):
        pn = (page - 1) * 25
        urlList.append(str(url)+str(pn))
    #构建head
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    #存放所有帖子链接
    linkList = []
    for url in urlList:
        html = requests.get(url).text;
        doc = pq(html)
        allPost = doc.find('table.olt tr');
        for post in allPost.items():
            linkList.append(post.find('td.title a').attr('href'));

        # content=etree.HTML(html)
        # #用xpath获取链接


    while None in linkList:
        linkList.remove(None)
    getImgLink(urls=linkList)










if __name__=="__main__":
    # url = input('请输入小组字符串代码如:haixiuzu')
    # beginPage = int(input('请输入起始页码'))
    # endPage= int(input('请输入结束页码'))
    url = 'blabla'
    beginPage = 1
    endPage=1
    #构建url
    url = 'https://www.douban.com/group/'+url+'/discussion?start='
    #获取所有url
    getPageLink(url,beginPage,endPage)