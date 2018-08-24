#!/usr/bin/env python
# coding: utf-8
"""
__author__ = zhongqiang

Created on  17/12/27

Describe: 
"""
from __future__ import unicode_literals
import argparse

"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

print args.accumulate(args.integers)
"""
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)

parser = argparse.ArgumentParser(prog='ttxs.py',
                                 usage='%(prog)s [options] 用法说明',
                                 description='A foo that bars 描述信息',
                                 epilog="And that's how you'd foo a bar 附加其他信息",
                                  # parents=[parent_parser]
                                 )

parser.add_argument('--foo',
                    # nargs='?',
                    required=True,
                    # metavar='YYY',
                    nargs=2,
                    metavar=('bar', 'baz'),
                    dest='bar',
                    help='foo of the %(prog)s program')
parser.add_argument('abc', nargs='+', help='abc help')
parser.add_argument('--bar', nargs='+', help='bar help')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.add_argument('--verbose', '-v', action='count')
parser.add_argument('-p', help='print 帮助信息')
parser.add_argument('--fab', '-f', default=42, type=int)
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# parser.parse_args(['--parent', '2', 'XXX'])
parser.print_help()     # 打印信息
args = parser.parse_args()

print args















