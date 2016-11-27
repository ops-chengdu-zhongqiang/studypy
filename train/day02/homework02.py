#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年4月9日

@author: zhongqiang

Describe: 
'''
from __future__ import unicode_literals
import  os

#打印某个文件夹下的所有文件
def All_file(folder):
    for i in os.listdir(folder):
        print i

#All_file('/Users/study/week02/basic_py/')


#备份文件名到指定文件-------->不支持文件夹名称有中文
def File_to_txt(folder):
    file1 = file('file01.txt','w')
    for i in os.listdir(folder):
        # print i
        if os.path.isdir(folder+i):
            file1.encoding
            file1.write(i+'\n')
            print "Dirname:%s" %i
    file1.close()

#File_to_txt('/Users/study/')



#过滤指定的名称的文件路径
def Get_file(folder,filetype):
    filelist=[]
    for i in os.listdir(folder):
        if os.path.split(i)[-1].split('.')[-1] == filetype:
            filelist.append(i)
            print i
    return filelist

#Get_file('/Users/study/week02/basic_py/','py')


#获取特定文件夹下特定类型的文件,返回完整路径
def Get_file_path(folder,filetype):
    filelist=[]
    for i in os.listdir(folder):
        if os.path.split(i)[-1].split('.')[-1] == filetype:
            filelist.append(folder+i)
            print folder+i
    return filelist

#print Get_file_path('/Users/study/week02/basic_py/','py')



#改造: list_my_dir函数-------->用列表解析改造上面的函数,打印可以略去
def list_my_dir(folder, use_yield=True):
    my_dir = []
    for i, file_x in enumerate(os.listdir(folder)):
        if i > 7:
            break
        elif i % 2 == 1:
            if use_yield:
                print file_x
                yield file_x
            else:
                my_dir.append(file_x)
        else:
            print 'hahahhha'
    if not use_yield:
        yield my_dir
        return

c =[i for i in list_my_dir(folder='/Users/webapp/',)]
print c




