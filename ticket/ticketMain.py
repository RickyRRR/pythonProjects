#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' buy ticket  '
__author__ = 'ricky Xu'


#python3.x

from splinter.browser import Browser
from time import sleep
# traceback模块被用来跟踪异常返回信息
import traceback
# 设定用户名、密码
username = u"869706005@qq.com"
passwd = u"xjf19920203"
# 起始站点和乘车时间的cookies值要去找；
# 方法：先登录一下12306，输入地点日期什么的查询一下，然后在chrome浏览器中按F12，出现如下页面，在Application选项里找到相应的值。
# 表格中的cookie值：
#_jc_save_fromeStation的值为出发地
#_jc_save_toSatation的值为目的地
#_jc_save_fromDate 出发日期
#_jc_save_toDate返程日期
# 实例中用的是：福州 到 厦门北 2018-01-13
from_station = u"%u53F0%u5DDE%2CTZH"
to_station = u"%u91D1%u534E%2CJBH"
# 时间格式2018-01-25
from_date = u"2019-02-03"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
# 设定乘客姓名
ticketer = u"徐剑锋"
# 设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"

login_url = "https://kyfw.12306.cn/otn/login/init"
newlogin_url = 'https://kyfw.12306.cn/otn/resources/login.html'

initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
newinit_myurl = "https://kyfw.12306.cn/otn/view/index.html"

# 登录网站
def login():
    #点击当前页面的"登录"
    bwr.find_by_text(u"登录").click()
    sleep(3)
    bwr.find_by_text("账号登录").click();
    sleep(1)
    #fill填充搜索框的内容，username。name=loginUserDTO.user_name的元素。
    # bwr.fill("J.user_name", username)
    bwr.find_by_id("J-userName").fill(username)
    sleep(1)
    # bwr.fill("J.password", passwd)
    bwr.find_by_id("J-password").fill(passwd)
    sleep(1)
    print(u"等待验证码，自行输入...")
    #登录手动输入验证码，并登录系统
    while True:
        #判断当前的url是否已经进入系统
        if bwr.url != newinit_myurl:
            sleep(1)
        else:
            break
# 购票
def getTickt():
    global bwr
    # 使用splinter打开chrome浏览器
    bwr=Browser(driver_name="chrome")
    # splinter打开浏览器（返回购票页面）
    bwr.visit(ticket_url)
    while bwr.is_text_present(u"登录"):
        sleep(1)
        login()
        #判断是否已经进入系统
        if bwr.url == newinit_myurl:
            break
    try:
        print(u"购票页面...")
        # splinter打开浏览器（跳回购票页面）
        bwr.visit(ticket_url)
        # 加载查询信息
        bwr.cookies.add({"_jc_save_fromStation": from_station})
        bwr.cookies.add({"_jc_save_toStation": to_station})
        bwr.cookies.add({"_jc_save_fromDate": from_date})
        bwr.reload()
        sleep(4)
        count=0
        # 循环点击预订
        if order != 0:
            while bwr.url == ticket_url:
                bwr.find_by_text("查询").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                sleep(1)
                try:
                    bwr.find_by_text(u"预订")[order - 1].click()
                except:
                    print(u"还没开始预订")
                    continue
        else:
            while bwr.url == ticket_url:
                 bwr.find_by_text(u"查询").click()
                 count += 1
                 print(u"循环点击查询... 第 %s 次" % count)
                 sleep(1)
                 try:
                     for i in bwr.find_by_text(u"预订"):
                         print('aaa')
                         i.click()
                         sleep(1)
                 except:
                     print(u"还没开始预订")
                     continue
        sleep(5)
        # 可以通过修改sleep的参数来调整延时, 但延时不要太低, 防止被12306网站认为是刷票屏蔽掉.
        bwr.find_by_text(ticketer)[0].click()
        sleep(10)
        bwr.find_by_text("提交订单").click()
        sleep(3)
        #bwr.find_by_id(u"qr_submit_id").click()
        print(u"成功抢到一张宝贵的票")
    except Exception as e:
         print(traceback.print_exc())

if __name__ == "__main__":
    getTickt()