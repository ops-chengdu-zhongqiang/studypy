#!/usr/bin/env python
# coding: utf-8

'''
Created on 2016年9月26日

@author:  ttxsgoto
logging为python模块提供状态、错误、信息输出的标准接口
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

https://blog.igevin.info/posts/python-log/

'''
import logging

#  记录日志信息
logname = 'log.log'
logging.basicConfig(
    level=logging.INFO,  # 定义记录大于或等于日志级别
    format='[%(levelname)s] [%(asctime)s] --- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=logname,
    filemode='a',
)

logging.warning("log")

# 将日志输出到文件，同时打印匹配的级别到屏幕上
console = logging.StreamHandler()
console.setLevel(logging.INFO)  # 定义需要显示大于或等于日志级别
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] ------ %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.warning('log info111')

logging.debug('debug  msg')
logging.info('info msg')
logging.warn('warn msg')
logging.error('error msg')
logging.critical('critical msg')

###### 几个概念 ######
"""
- Logger记录器: 暴露了应用程序代码能直接使用的接口
- Handler处理器: 将记录器产生的日志记录发送到合适的目的地
- Filter过滤器: 决定输出哪些日志记录
- Formatter格式化器: 指明最终输出中日志记录的布局
"""

logger = logging.getLogger('logger_name')  # 创建logger记录器,返回一个logger实例，如果没有指定name，返回root logger,
# 只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的

logger.setLevel(logging.DEBUG)  # 设置logger的level
logger.addHandler()  # 加handler来帮它处理日志,StreamHandler:输出到控制台,FileHandler:输出到文件

logging.basicConfig('**kwargs')  # 用来配置root logger， 为root logger创建一个StreamHandle
