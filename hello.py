#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'
import sys



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

print(ricky)
