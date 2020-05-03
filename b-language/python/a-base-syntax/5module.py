#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行可以让该文件直接在linux上运行
# 第二行注释，表示使用utf-8解码


# 表示模块的文档注释(任何模块的第一个字符串都会被认为是模块的文档注释)
'a test module'

# 将作者作为变量写进去
__author__ = 'huixiong'

# 删除所有的中文注释就是标准的模块模板
import sys


def test():
    # 获取输入的命令list，例如 python module.py 
    args = sys.argv
    if len(args) == 1:
        print("Hello Stupid %s" % args[0])
    elif len(args) == 2:
        print('Hello,%s' % args[1])
    else:
        print('go away~')

if __name__ == '__main__':
    test()

#-----------------------------------
# 其他注释
# 必须导入 sys 模块才行
# sys中有一个argv变量,用于存储命令行所有参数。至少有一个参数，即*.py 
# 运行 python module.py 获取的sys.argv 就是['module.py']
# 最后两行。当执行.py 文件时,python解释器会把一个特殊变量 __name__置为'__main__'
# 如果在其他地方导入了就不会执行。

# 作用域

# 特殊变量名，可以被直接访问，但通常由特殊用途。一般不这样命名。
__test__ = 'test'

# public变量
a = 'asf'

# private变量,同样可以直接访问，但是不建议直接访问。是一种编程习惯
_p = 'private'

# 另外，如果需要可以使用Anaconda,一个基于Python的数据处理和科学计算平台

#------------------------
# 模块的目录结构 https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176

#------------------------
# 常用内建模块 https://www.liaoxuefeng.com/wiki/1016959663602400/1017648783851616

#------------------------
# 常用第三方模块  https://www.liaoxuefeng.com/wiki/1016959663602400/1017785364772448
