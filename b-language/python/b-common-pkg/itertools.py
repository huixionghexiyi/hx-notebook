# 提供常用的迭代器

import itertools
naturals = itertools.count(1)# 无线循环
# for i in naturals:
#     print(i)

# cs = itertools.cycle('ABCD') # 无线循环序列,一个一个的输出
cs = itertools.repeat('ABCD',3) # 有限循环，每次都输出 ABCD
for i in cs:
    print(i)

naturals = itertools.cycle('ABCD')
ns = itertools.takewhile(lambda x: x!='D',naturals) # 对无线循环序列增加终止条件
for i in ns:
    print(i)
# print(list(ns))

ch = itertools.chain('ABC','DEF')# 串联几个迭代对象为一个大的迭代对象
for i in ch:
    print('chain:'+i)

gb = itertools.groupby('AAABBBCCCAAA')# 将相邻的重复元素进行分组,每一组都是可迭代对象
for key,li in gb:
    print(key,list(li))
