#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年4月24日

@author: zhongqiang

Describe: 多进程-Pool
'''

from multiprocessing import Pool
import time

def f(x):
    print x*x
    time.sleep(1)
    return x*x

pool = Pool(processes=5) #最多5个进程
res_list = []


print "------------"
print "执行方法一"
#执行方法一
print pool.map(f,range(10))  #将函数放在5个进程中执行


print "end 01 -------"

#执行方法二
print "执行方法二"
for i in range(10):
    res = pool.apply_async(f,(i,)) #apply_async 设置为异步
    #res.get() #取线程执行的结果
    res_list.append(res)  #将执行结果放入列表中
  
for r in res_list: #循环列表得到结果
    print r.get()

print "Over over ..."

















    
    







