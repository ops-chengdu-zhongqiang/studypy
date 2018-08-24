#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/5

Describe:
https://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652564462&idx=2&sn=24e2333782804b68f7a760b186f84c83&chksm=8464c3a4b3134ab2fc2d6e13726e8df38aa424c5b4b95d77f4fcb36612f9c1bfc13f43e469de&scene=0&key=4489c38d1d617d5cdd3fb38f5c22680c6a89487202cb85b1aacb34ad5a1c8266fd30b81e26fde9177d80962462df60784d9396ace3bb7521171a88ce1bfc195030092c471cab9df25d811437849b4265&ascene=0&uin=MTg0NTIzNDI4MA%3D%3D&devicetype=iMac+MacBookAir7%2C2+OSX+OSX+10.10.5+build(14F27)&version=12010210&nettype=WIFI&fontScale=100&pass_ticket=KXkH0COd4rzEHNW0VEbvhf1SHJXJw9uPnymIU%2B2mQHFXta1G8si7ta44%2Bf7pjXWM
https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
'''
import time

from celery_app import task1
from celery_app import task2

print "异步执行开始:",time.ctime()
task1.add.apply_async(args=(2,8), countdown=5) # 5 秒后执行任务
task2.multiply.delay(3,7)

print "end!!!!!"
print time.ctime()



