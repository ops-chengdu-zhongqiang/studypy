#!/usr/bin/env python
# coding: utf-8
"""
__author__ = zhongqiang

Created on  17/12/27

Describe:
    - optparse 用法
    - add_option()中参数
        - dest 可以决定后来取值时的名字(parse后的options的属性名), 尤其适于有多个等价参数. 不指定时就是选项不加-的字符串
        - type: 默认选项对于的值是字符串, 这里可以指定别的类型
        - default: 缺省值. 没有设置缺省值的为None
        - help: -h选项使用时打印的help
        - metavar: 表示显示到help中option的默认值
        - choices: 当设置type为choices时，需要设置此值
        - const: 指定一个常量值给选项, 该常量值将用于后面store_const和append_const
        - action: 控制对选项和参数处理,像无参数选项
            - store: 储存值到属性,强制要求后面提供参数(缺省)
            - store_true: 当使用该选项时,后面的dest将设置为true. 不跟参数
            - store_false: 当使用该选项时,后面的dest将设置为false. 常配合另一个store_true选项使用同一个dest时使用. 不跟参数
            - append: 将后面的值追加到dest的列表中, 必须跟参数
            - store_const: 将相应const对于的值储存给dest,常用于同dest名2个以上选项时的处理. 不跟参数.
            - append_const: 将相应const的值追加给dest列表. 不跟参数
            - count: 使用后将给后面的计数器加1,可以统计参数中出现次数.
            - callback: 后面指定回调函数名(不加括号),会将相应opt和args传给回调函数
            - help, version: 对应为帮助和版本. 要另外自己设计时使用
相关函数:
    - set_default(dest1=value1,dest2=value2..): 可以用来同时设置多个选项的默认参数
    - has_option(opt): 检查是否有相应选项(使用相应-f里的f)
    - remove_option(opt): 删除选项(使用相应-f里的f)


"""

from __future__ import unicode_literals
from optparse import OptionParser

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    (options, args) = parser.parse_args()   # 解析程序的命令行
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print "reading %s..." % options.filename

if __name__ == "__main__":
    main()


