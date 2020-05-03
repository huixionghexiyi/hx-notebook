# python 的高级特性
# 我们先回顾四种基本集合 list、tuple、dict、set

# list = [1,2,3] 其中元素可以位任意类型、有顺序、可变，查找、插入的时间随元素的增加而增加。内存占用小

# tuple = (1,2,[5,1]) 其中元素可以位任意类型，包括list等集合，有序、不可变、不能修改

# dict = {"name":18,"name2":19,"name3":20} 其中元素可以位任意类型，类似于map ，无序，查找快、内存消耗大

# set = ([1，2，3]) 其中元素可以是任意类型，可以看成不存储value的dict

# 切片 按照左闭右开的取法 ,数学上表示成 [0,2)，即取 0，1 两个位置的元素

from collections.abc import Iterator, Iterable
import os
name = ["name1", "name2", "name3", "name4"]

for i in name[0:2]:
    print(i)
print("-----------")
for j in name[-3:]:  # 注意：倒数的第一个元素是 -1
    print(j)
nums = list(range(100))  # 从0开始 取100个数放到list中
i1 = nums[:10]  # 前十个
i2 = nums[-10:]  # 后十个
i3 = nums[10:20]  # 指定11-20
i4 = nums[:10:2]  # 划分前十个，每隔2个取一个。
i5 = nums[:10:-2]  # 划分前十个，再倒着取，每个两个取一个，取到划分处
i6 = nums[:-10:-2]  # 划分后10个，倒着取，每隔两个取一个，取到划分处
i7 = nums[:-10:2]  # 划分后十个，正着取，每个2个取一个，取到划分处
i8 = nums[::4]  # 所有数，每隔4个取一个
print(i8)
# tuple 也可以切片，切片后任是tuple
tu1 = tuple(range(10))
t1 = tu1[:3]
t2 = tuple(range(10))[:3]
# 数组也可以切片
s1 = 'ABCDEF'[:-3]
print(s1)

# 去除首尾的空格
s = ""
# s = "   fu   hello  "
while s[:1] == ' ':  # 不适用是s[0]作为第一个元素判断依据的原因是避免字符串为空时的空指针情况。
    s = s[1:]
while s[-1:] == ' ':
    s = s[:-1]

print(s)

# ----------------------------------------------------------------------
# 迭代

# 迭代dict
d = {"age1": 12, "age2": 10, "age3": 19}
for key in d.keys():  # 迭代key值
    print(key)

for value in d.values():  # 迭代value
    print(value)

for k, v in d.items():  # 迭代key和value
    print(str(k)+"--"+str(v))  # 将 int转换成str 才能用连接符号

for ch in 'ABC':  # 迭代字符串
    print(ch)

# 当我们需要使用for循环时，只需要作用于一个可迭代的对象即可，for循环就可以正常运行。而不需要关心对象究竟是什么类型。

# 那么判断一个对象是否可迭代就变得重要了。

from collections.abc import Iterable  # 引入package
print(isinstance('abc', Iterable))  # True

# 对list的下标进行循环
for iii, ii in enumerate(['A', 'B', 'C']):
    print(iii, ii)
# 同时引用两个变量（在python中这是非常常见的）
for x, y in [(1, 1), (3, 6), (2, 7)]:
    print(x, y)

# ----------------------------------------------------------
# 列表生成式

# 生成1到10的平方
# 方式一 循环
li = []
for x in range(1, 11):
    li.append(x*x)
# 方式二 列表生成式
li = [x*x for x in range(1, 11)]
# li = list(range(1,11))
for x in li:
    print(x)

# 使用两层循环 m 从'ABC'中取，n 从'XYZ'中取，再拼接
[m + n for m in 'ABC' for n in 'XYZ']

# 案例，列出当前目录下的所有文件和目录名
import os
[d for d in os.listdir('.')]

# 同时使用两个变量生成list
d = {"1": "1", "2": "2", "3": "3", "4": "4"}
[k+"="+v for k, v in d.items()]
# 全变小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
# ---------------------------------------
# 生成器(generator)
# 特点，我们不必像list生成式那样，真正的将list存到内存中。但是generator只能顺序输出，相当于，在我们使用的时候才执行。
# 斐波那契数列的generator
from collections.abc import Iterable,Iterator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        try:
            # print(b)
            yield(b)  # 这里就是要通过这个函数输出的值。
            a, b = b, a+b
            n = n+1
        except StopIteration as e:
            print("the return is :", e.value)
            break
    return 'ok'


f = fib(10)  # f指向该函数,Iterable,Iterator
# 每执行一次next，就会在yield处中断，下次再调用next就会接着终端执行
print(next(f))
print(isinstance(f,Iterator))
from collections.abc import Iterable,Iterator
# 使用迭代
for n in fib(10):
    print(n)
# 要想获取return的返回值，必须捕获异常StopIteration

# ---------------------------------------
# 迭代器(Itertor)
# 属于Iterable类型的对象才能用for迭代
# 判断的方式是
from collections.abc import Iterable,Iterator
isinstance([], Iterable)
# for循环本质上就是不停的调用next()
# 判断方法
isinstance([(1, 1)], Iterator)
# 将list、tunple、str、dict、set 5个基本类型变成Iterator，就可以使用next()进行迭代
iter('abc')
