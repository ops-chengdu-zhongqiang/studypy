#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/13

Describe: 
'''

# !/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/13

Describe:
    - 读取excel数据
    - pip install xlrd
'''
import os

# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
# application = get_wsgi_application()

import xlrd


def open_excel(file='file.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print e


def writer_into_db(file=None):
    data = open_excel(file)
    table_name = data.sheet_names()
    # table = data.sheet_by_name(u'Sheet1') # 通过名称获取table
    table = data.sheets()[0]  # 通过索引顺序获取
    table = data.sheet_by_index(0)  # 通过索引顺序获取
    print table_name
    print table.nrows  # 所有行数
    print table.ncols  # 所有列数
    print table.cell(2, 2).value  # 获取某单元格的值

    nrows = table.nrows
    fields = []
    for row in range(1, nrows):
        print table.row_values(row)[2]

        # fields.append(ReportField(
        #     id=int(table.row_values(row)[0]),
        #     title=table.row_values(row)[1],
        #     field_title=table.row_values(row)[2],
        #     type=table.row_values(row)[3],
        #     field_type=table.row_values(row)[4],
        #                           )
        # )
    # try:
    #     ReportField.objects.bulk_create(fields)
    # except Exception as e:
    #     return False, str(e)
    return True


if __name__ == '__main__':
    # file = '/Users/zhongqiang/Downloads/2.xlsx'
    file = 'hello.xlsx'
    if writer_into_db(file):
        print 'insert success!!!'
    else:
        print 'insert failed'
