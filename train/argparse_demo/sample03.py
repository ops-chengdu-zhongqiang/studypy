#!/usr/bin/env python
# coding: utf-8
"""
__author__ = zhongqiang

Created on  17/12/27
http://blog.xiayf.cn/2013/03/30/argparse/
Describe:
    - add_argument() 方法的 action 参数指定
        参数说明:
        - store 保存参数
        - store_const 保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值
        - store_ture/store_false 保存相应的布尔值
        - append 将值保存到一个列表中。若参数重复出现，则保存多个值
        - append_const 将一个定义在参数规格中的值保存到一个列表中
        - version 打印关于程序的版本信息，然后退出

    - parse_args() 传递一组参数字符串来解析命令行,默认情况下，参数是从 sys.argv[1:] 中获取，但你也可以传递自己的参数列表
        - 返回值是一个命名空间，包含传递给命令的参数, 可通过args.option来访问对应的参数
"""

from __future__ import unicode_literals
import argparse

'''
parser = argparse.ArgumentParser(description='This is a Py sample program')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
print parser.parse_args(['-a', '-bval', '-c', '3'])
'''

'''
parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', '-n', action="store_true", default=True)
parser.add_argument('--witharg', action="store", dest="witharg", default='abc')
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

args = parser.parse_args()

# args =  parser.parse_args(['-n', '--witharg', 'val', '--witharg2', '23'])
print args.noarg, args.witharg, args.witharg2
'''

####################################################
#   基本用法
# nargs 可变形参列表
#   - N   参数的绝对个数（例如：3）
#   - ?   0或1个参数
#   - *   0或所有参数
#   - +   所有，并且至少一个参数
#
# argparse将所有参数值都看作是字符串，可指定type来转换为对应的类型,如 int, float, file等
####################################################


def main(**kwargs):
    print kwargs
    return kwargs

def get_parser():
    parser = argparse.ArgumentParser(
        prog='ttxs.py',
        # usage='%(prog)s [options] 用法说明',
        description='A foo that bars 描述信息',
        epilog="And that's how you'd foo a bar 附加其他信息",
        add_help=True,   # help信息, 默认添加
        version='%(prog)s 1.1.0'    # 添加版本信息,也可以在后面参数定义

    )

    parser.add_argument('-s', action='store', dest='simple_value',  # args.simple_value对应的引用值
            # nargs=3,        # 指定参数为3个数
            # nargs='+',      # 至少一个参数
            type=int,
            default='12',
            help='Store a simple value',)

    parser.add_argument('-c', action='store_const', dest='constant_value',
            const='value-to-store', # 这里使用-c参数,对应的值为value-to-store
            default='store_const', # 默认值
            help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=True,
            dest='boolean_switch',
            help='Set a switch to true')

    parser.add_argument('-f', action='store_false', default=False,
            dest='boolean_switch',
            help='Set a switch to false')

    parser.add_argument('-a', '--alist', action='append', dest='collection',   # append 将值保存到list中
            default=[],
            help='Add repeated values to a list')

    parser.add_argument('-A', action='append_const', dest='const_collection', # 使用参数将const定义的保存到list中
            const='value-1-to-append',
            default=[],
            help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
            const='value-2-to-append',
            help='Add different values to list')
    results = parser.parse_args()
    return results

results = get_parser()
print 'simple_value     =', results.simple_value
print 'constant_value   =', results.constant_value
print 'boolean_switch   =', results.boolean_switch
print 'collection       =', results.collection
print 'const_collection =', results.const_collection

if __name__ == '__main__':
    results = get_parser()
    data = {
        'simple_value': results.simple_value,
        'constant_value': results.constant_value,
        'boolean_switch': results.boolean_switch,
        'collection': results.collection,
        'const_collection': results.const_collection
    }
    main(**data)

