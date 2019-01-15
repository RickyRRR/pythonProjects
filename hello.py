#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'
import sys
import logging
from io import StringIO
import os
logging.basicConfig(level=logging.INFO)
#


print("hello!");

# print(ord('A'));
# print(chr(65))

print('rate is %.2f %% ' % 3.14);  #占位符

b = '中文'.encode('utf_8')  # 转换成bytes
b1 = 'a'.encode('ascii')



#birth = input('请输入：');
# print(birth)

n1 = list(range(5));   #range(5)生成的序列是从0开始小于5的整数


# list [] y有序  append(1) pop   insert  sort
# tuple()不可变有序     key in dict判断dict中是否存在该key

# dict{} 无序key不能重复  dict.get("key") 不存在返回None 或者d.get('key',-1)返回-1     dict['key']
# pop(key)  需要牢记的第一条就是dict的key必须是不可变对象。string  int不可变

# set  add(key)  remove(key)
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# s1 & s2  s1 | s2    并集交集操作



# 函数 abs max int() float()  str(123)  bool(1)
# 可变参数
# def cals(*num):   函数内部把num作为tuple处理
# 关键字参数
# def person(name,age,**other):  other作为dict处理
# extra = {'city': 'Beijing', 'job': 'Engineer'}     person('xiaoming',25,city='hangz',sex='male') 或者person('Jack', 24, **extra)
# def total(a=5,*number,**phonebook):
#     print('a',a);
#
#     for single_item in number:
#         print('single_item',single_item);
#
#     for first,second in phonebook.items():
#         print(first,second)
#
# print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
#help(print_max);
# for i, value in enumerate(['A', 'B', 'C']):   有key也有value
#     print(i, value)
# L = [x * x for x in range(10) if x%2==0]   #列表生成式
# g = (x * x for x in range(10) if x%2==0)   #生成器
# for n in g:
#     print(n)

def odd():
    print('s1');
    yield (1);
    print('s2');
    yield 2;
    print('s3');
    yield 3;

# o= odd();
# n1 = next(o);
# n2 = next(o)
# next(o)

def is_odd(n):
    return n%2==1;
# r = filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]);
# list = list(r);
# print(list)
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_score(t):
#     return t[1];
# newL = sorted(L,key=by_score,reverse=True);
# print(newL)


class Student(object):
    city='hz';
    def __init__(self, name, score, sex):  # 有点像构造函数
        self.name = name;
        self.score = score;
        self.__sex = sex;  # 私有变量

    def __print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_sex(self):
        return self.__sex;
    def set_sex(self,sex):
        self.__sex = sex;
    def set_city(self):
        city='jh'
        return city

ricky = Student('ricky',95,'male');
rickySex = ricky.get_sex();
ricky.set_sex('female')
rickySex = ricky.get_sex();
a = ricky.city;
a = ricky.set_city();
masa = Student('masa',95,'female');

class Animal(object):
    def run(self):
        print('animal is running...');
class Dog(Animal):
    def run(self):
        print('dog is running...');
def run_twice(Animal):      #多态  根据实际传参调用具体的run方法
    Animal.run();
dog1 = Dog();
animal = Animal();
isAnimal = isinstance(dog1,Animal);
dog1.run();

L = dir('ABC')
#
# try:
#     r= int('a');
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# try:
#     r = 10/int('a');
#     print('result:'+r);
# except ZeroDivisionError as e:
#     print('zeroExcept:'+e);
# except ValueError as e:
#     print('valueExcept:'+e)
# finally:
#     print('finally...');


#管道f
try:
    f = open('reHello.txt', 'r');
    #str = f.read();
    # strList=f.readlines()  #line.strip()    删掉行末尾的\n

    str=''
    s=''
    while True:
        s = f.read(2);
        if s == '':
            break;
        print(s.strip())


except BaseException as e:
    print(e)
    #logging.info('readFile:'+e);
finally:
    if f:
        f.close();
with open('reHello.txt', 'r') as f:
    f.read();

ff = StringIO();
ff.write('hi man');
ffstr = ff.getvalue()

oss = os.environ

#os.rename('hello.txt','reHello.txt')


print(ricky)
#print('{0:_^11}'.format('hello'))

# str1 = 'abchjk'
# listStr1 = list(str1);
# listStr1.reverse();
# print(listStr1)
# p = '-'.join(listStr1);

list = [1,2,3,4];
print(list[::-2])
