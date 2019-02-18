#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a wechat  '
import base64
import re
import schedule
import time
__author__ = 'ricky Xu'


from wxpy import *

import json
import requests


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_replytulin(text):
    # print(23)
    url = "http://www.tuling123.com/openapi/api"
    api_key = "c47f1d00a518455daf7ff4fcc6471982"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    # print(12)
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "" + result["text"]


bot = Bot(cache_path=True)
print(type(bot));

allgroups = bot.groups();
# print(allgroups)
# 搜索名称包含 '游否' 的深圳男性好友
# found = bot.friends().search('恬', sex=MALE, city='深圳')
# [<Friend: 游否>]
# 确保搜索结果是唯一的，并取出唯一结果
# youfou = ensure_one(found)
# <Friend: 游否>



# 搜索名称包含 'wxpy'，且成员中包含 `游否` 的群聊对象
# wxpy_groups = bot.groups().search('wxpy', [youfou])
# [<Group: wxpy 交流群 1>, <Group: wxpy 交流群 2>]

# 将老板的消息转发到文件传输助手
# @bot.register(company_group)
# def forward_boss_message(msg):
#     if msg.member == boss:
#         msg.forward(bot.file_helper, prefix='老板发言')


# 堵塞线程
# embed()



myself = bot.friends().search('Xu🍃')
# boring_group = bot.groups().search('每天进步一点点')[0]
enjoyhai = bot.groups().search('嗨起来')
# print(enjoyhai)
# my_friend1 = boring_group.search('小张')[0]


# my_friend.send('Hello, wechart!')
# profile = my_friend.get_avatar(save_path='test.jpg');
# bot.file_helper.send("hello  nihao")
# bot.self.send('能收到吗？')
# @bot.register([ boring_group])
# def auto_reply(msg):
#
#     if msg.member == my_friend1 and msg.type == 'Text':
#
#         return auto_replytulin(msg.text)
#
#
#     # 如果是群聊，但没有被 @，则不回复
#     if isinstance(msg.chat, Group) and not msg.is_at:
#         return
#     else:
#         # 回复消息内容和类型
#         return auto_replytulin(msg.text)


# @bot.register([ enjoyhai],except_self=False)
# def rep(msg):
#     # print(msg.member)
#     if msg.member == my_friend:
#         print('llll')
#         return auto_replytulin(msg.text)
#
#
#
friendone = bot.friends().search('胡薰尹')[0]
@bot.register([bot.self],except_self=False)
def print_message(msg):
     return auto_replytulin(msg.text)

@bot.register([friendone],except_self=False)
def print_message(msg):
     return auto_replytulin(msg.text)
# def write_txt_file(path, txt):
#     '''
#     写入txt文本
#     '''
#     with open(path, 'a', encoding='gb18030', newline='') as f:
#         f.write(txt)
#
#     # 统计签名
#
#
#     for friend in bot.friends():
#         # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
#         pattern = re.compile(r'[一-龥]+')
#         filterdata = re.findall(pattern, friend.signature)
#         write_txt_file('signatures.txt', ''.join(filterdata))
#




def generateSign():

    tList = []
    # print(bot.friends())
    for i in bot.friends():
        # print(i.signature)
        # 获取个性签名
        signature = i.signature.strip().replace("span", "").replace("class", "").replace("emoji", "")
        # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
        rep = re.compile("1f\d.+")
        signature = rep.sub("", signature)
        tList.append(signature)
        # print(signature)

    # 拼接字符串
    text = "".join(tList)

    # jieba分词
    import jieba
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)

    # wordcloud词云
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import PIL.Image as Image

    # 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
    my_wordcloud = WordCloud(background_color="white", max_words=2000,
                             max_font_size=40, random_state=42,
                             font_path='C:/Windows/Fonts/simkai.ttf').generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.savefig("filename.png")
    plt.show()


# generateSign()

# 定时发送任务
# def job():
#     print("I'm working...")
#
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
# 进入Python命令行，让程序保持运行
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def postMyApi():
    friendList = [];
    groupList = [];
    mpList= []
    friends = bot.friends()[0:8];
    for friend in friends:
        friendDict = {'name':friend.name,'sex':friend.sex,'city':friend.city,'signature':friend.signature}
        friendList.append(json.dumps(friendDict,ensure_ascii=False));
    # print(infoList)
    for group in bot.groups():
        groupDict = {'name':group.name};
        groupList.append(json.dumps(groupDict,ensure_ascii=False))
    for mp in bot.mps():
        mpDict = {"name":mp.name};
        mpList.append(json.dumps(mpDict,ensure_ascii=False));


    content= {"friends":' '.join(friendList),"groups":' '.join(groupList),"mps":' '.join(mpList),"selfname":bot.self.name}

    r = requests.post('http://154.8.225.214:8080/collect/WechatServlet', data=content);


def is_myFriend():
    count1 = 0
    count2 = 0




    group1 = bot.groups().search('嗨起来');
    if len(group1) > 0:
        print(group1[0]);
        dog = bot.friends().search('邬王二狗')[0];

        group1[0].add_members(dog);

    # for member in group1:
        # member.send_msg(" ॣ ॣ ॣ");

def historyMsg():
    bot.self.send('bbbbbb')
    sent_msgs = bot.messages.search(sender=bot.self)
    print(sent_msgs)

# postMyApi()
# is_myFriend();
historyMsg()
embed()

# text = bot.friends().stats_text()
# print(text)
# 游否 共有 100 位微信好友\n\n男性: 67 (67.0%)\n女性: 23 (23.0%) ...