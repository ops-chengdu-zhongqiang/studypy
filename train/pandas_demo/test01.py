#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/20

Describe:
    - pip install pandas

http://wiki.jikexueyuan.com/project/start-learning-python/311.html
http://shujuren.org/article/207.html
http://blog.csdn.net/yhb315279058/article/details/50226027
http://www.jianshu.com/p/96447bee3961
https://ericfu.me/10-minutes-to-pandas/

https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=2651435170&idx=1&sn=1a112bead78327a672ebb1c2d2167b4f&scene=21#wechat_redirect
https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=2651435212&idx=1&sn=86ab8a363c590e841c6e9e5615bf8c45&scene=21#wechat_redirect
'''

from pandas import Series, DataFrame
import pandas as pd


# 读取excel文件内容
# sheetname 对应的sheet,可以为数字和内容
context = pd.read_excel('default_fields.xlsx',
                        sheetname=2,
                        header=0,
                        encoding = 'utf-8',
                        na_values=['NA'], index_col=None)

# print type(context)
print context.head()
print context   # 表内容
print context.columns   # 查看有哪些列
print context['id'], #context['report_structure']


# 写入excel文件
data=[1,2,3,4,5]
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]
        }


df = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
# print df

writer = pd.ExcelWriter('test.xlsx')
df.to_excel(writer, sheet_name='test')
writer.save()




















