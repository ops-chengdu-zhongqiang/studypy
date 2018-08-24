#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/13

Describe:
    - 读写excel文件
    - pip install openpyxl
    - http://liyangliang.me/posts/2013/02/using-openpyxl-to-read-and-write-xlsx-files/
'''

from openpyxl import load_workbook, Workbook


wb = load_workbook('./hello.xlsx')
sheets = wb.get_sheet_names()   # 获取表格名称列表
print sheets[0]
ws = wb.get_sheet_by_name('Sheet1')
print ws.rows   # 行
print ws.columns    # 列
content = []
for row in ws.rows:
    line = [col.value for col in row]
    print line
    content.append(line)

# print content








