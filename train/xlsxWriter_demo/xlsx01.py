#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年11月27日

@author: zhongqiang

Describe: 
'''
import thread
import xlsxwriter
'''
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
workbook.close()
'''
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')   
worksheet = workbook.add_worksheet('test')
# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)
# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0
# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1
# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')
workbook.close()

#=============================







