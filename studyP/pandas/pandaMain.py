#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'

import pandas as pd
import xlrd




def readFile():
    # 方法一：默认读取第一个表单
    df = pd.read_excel('test1.xlsx',sheet_name='Python')  # 这个会直接默认读取到这个Excel的第一个表单
    data = df.ix[1,2]
    #data = df.values()  # 默认读取前5行的数据
    print(type(data))
    # print("输出值", df.sample(1).values)  # 这个方法类似于head()方法以及df.values方法
    # print("获取到所有的值:\n{0}".format(data))  # 格式化输出

    print(df.columns.values)
    data2 = df.ix[[0,2],['name','age','course','fee']]
    print(type(data2))
    row_data = df.ix[0, df.columns.values].to_dict()
    print(row_data)
    print(type(row_data))
def readFile1():
    df = pd.read_excel('test1.xlsx', sheet_name='Python')  # 这个会直接默认读取到这个Excel的第一个表单
    #print(df['age'][])
    # df1 = df[['name','age']]
    # df2 = df.loc[df['name']=='ric'].loc[df['status']==1]
    df3 = df['姓名']
    set1 = set()



    sum_name_age_list = [['name','age']]
    sum_name_age_list = []
    for i in df3:
        set1.add(i)


    for name in set1:
        temp = []
        df4 = df.loc[df['姓名']==name]
        temp.append(name)
        tempage = df4['年龄'].sum()
        temp.append(tempage)
        sum_name_age_list.append(temp)
        # temp.append(df4['age'].sum())
        # print(df4)
        # print('\r\n')

    print(sum_name_age_list)

    summaryDataFrame = pd.DataFrame(sum_name_age_list,columns=['name','age'])
    olddf = pd.read_excel('newTest1.xlsx')

    print(summaryDataFrame)
    print(olddf)
    newdf = pd.concat([olddf,summaryDataFrame],ignore_index=True).to_excel('newTest1.xlsx', encoding='utf-8', index=False, header=False)
    print(newdf)
    # print(df1)
    # print(df2)
    # print(type(df['status']))
    # arr = df['status']
    # for i in arr:
    #     print(i)
def readFile2():
    df = pd.read_excel('test1.xlsx', sheet_name='Python')
    df1 = pd.DataFrame(df,columns=['姓名','年龄'])
    df1['newCol'] = ['lal','bb','cc','dd']
    df1['newCol'] = df1['newCol'].replace('dd','ee')
    print(df1)
if __name__ =='__main__':
    readFile1()