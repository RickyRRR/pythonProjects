#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 爬取杭州豆瓣信息 '
import requests
from pyquery import PyQuery as pq
__author__ = 'ricky Xu'
import sys
import logging
from io import StringIO
import os
import urllib.request
from PIL import Image
from io import BytesIO
import io
def getimg():
    file_path = 'book/img'
    file_name = "pyt"
    # 判断目录是否存在
    isExists = os.path.exists('./img')
    # 如果不存在创建
    if not isExists:
        os.makedirs('./img')
    url = 'https://img3.doubanio.com/view/group_topic/l/public/p142123203.webp'
    res = requests.get(url);

    byte_stream = io.BytesIO(res.content)  # 把请求到的数据转换为Bytes字节流
    roiImg = Image.open(byte_stream)  # Image打开Byte字节流数据

    imgByteArr = io.BytesIO()  # 创建一个空的Bytes对象

    roiImg.save(imgByteArr, format='PNG')  # PNG就是图片格式，我试过换成JPG/jpg都不行

    imgByteArr = imgByteArr.getvalue()  # 这个就是保存的图片字节流

    # 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
    with open("./img/a.png", "wb") as f:
        f.write(imgByteArr)

    # with urllib.request.urlopen(
    #         url, timeout=30) as response, open("lyj.png"
    #     , 'wb') as f_save:
    #     f_save.write(response.read())
    #     f_save.flush()
    #     f_save.close()
    #     print("成功")







if __name__ == '__main__':
    strtest = 'lalal/123.jpg'
    strtest = strtest[-7:-4]
    print(strtest)
    res = requests.get(None)
    print(res.text)
    #getimg();