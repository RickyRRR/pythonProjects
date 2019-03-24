#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '
__author__ = 'ricky Xu'

from multiprocessing import Process
import os
import time


def test(arg):
    print(arg)
    time.sleep(4)
    print("the process %s is executing "%os.getpid())


p1 = Process(target=test, args=("hahaaaaaa",))  # 以元组的形式传递参数
p1.start()

p1.join(timeout=2)  # 子进程执行结束之后主进程才继续往下执行
# timeout设置超时时间 超过这个时间如果子进程还没结束 主进程将继续执行

# p1.terminate()  # 杀死p1进程

print("finish")  # 主进程执行完之后并不会关闭 而是会等子进程执行结束再关闭


# 类似Java多线程  继承Process类  重写run方法 实例化 start调用
class MyProcess(Process):

    def run(self):
        time.sleep(3)
        print("haha...")


m1 = MyProcess()
m1.start()
print("主进程执行到这里了....")