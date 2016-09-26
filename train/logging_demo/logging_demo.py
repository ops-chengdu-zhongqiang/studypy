#!/usr/bin/env python
#coding: utf-8

'''
Created on 2016年9月26日

@author:  ttxsgoto
logging为python模块提供状态、错误、信息输出的标准接口
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
'''
import logging

#  记录日志信息
logname = 'log.log'
logging.basicConfig(
    level = logging.INFO,	#定义记录大于或等于日志级别
    format='[%(levelname)s] [%(asctime)s] --- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=logname,
    filemode='a',                
    )

logging.warning("log")

#将日志输出到文件，同时打印匹配的级别到屏幕上
console = logging.StreamHandler()
console.setLevel(logging.INFO)	#定义需要显示大于或等于日志级别
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] ------ %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.warning('log info')






