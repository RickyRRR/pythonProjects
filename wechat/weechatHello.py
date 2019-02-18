import json
import re

import requests


def getMyApi():
    data = '''
        [{"a":1,"b":2}]
    '''
    content = {'info': data}
    r = requests.get('http://localhost:8082/timTest/WechatServlet', params = content)
    print(r.url)
def postMyApi():
    str = '''
       [{"a":1,"b":2}]
    '''
    dict={"a":"啦啦啦哈哈哈","age":"bbb"}
    dict1 = {"a": "baaa", "age": "bbccccb"}
    list = []
    list.append(json.dumps(dict,ensure_ascii=False));
    list.append(json.dumps(dict1,ensure_ascii=False));
    print(list)
    strlist = ' '.join(list)
    content = {'info':strlist}
    r = requests.post('http://localhost:8082/timTest/WechatServlet', data = content);
    print(r.url)

def readweChatTxt():
    path = "D:/Program Files/apache-tomcat-8.5.34/webapps/timTest/appendfile.txt";
    with open(path,'r') as f:
        content = f.read();
        infoList = content.split('--')
        print(infoList)

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title
# postMyApi();
# readweChatTxt();'Xu🍃'
print(validateTitle('Xu🍃'));
# testDict = {"name":"啦啦啦"}
# print(json.dumps(testDict,ensure_ascii=False));