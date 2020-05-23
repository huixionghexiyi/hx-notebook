
# 高阶函数
# 回顾一下Iterable（可迭代的）和Iterator（迭代器）
# 可迭代的是哪几种基本数据类型：tuple、list、dict、set、str。当然包括列表生成器生成的list
# 迭代器:generator（生成器）生成的类型就是迭代器。不直接占用内存，需要的时候再运算出来。
# 可以是一个值，也可以是一个函数。
# 函数用yeild中断，添加到循环部分即可。

# map(def,Iterable),将一个Iterable通过指定的函数转换成Iterator。返回一个Iterator
def f(x):
    return x*x
r = map(f,[1,2,3,4,5])
for i in r:
    print(i)
# 输出[1,4,9,16,25]
next(r)

def xx(x):
    print(x)
    return x

rr = map(xx,[1,2,3])

next(rr)
# --------------------------------------------------------
# reduce(def,Iterable),将def作用到Iterable的所有元素上。返回一个参数
# 拼接一个数组成字符串
from functools import reduce

def fff(x,y):
    # print(str(x)+"==="+str(y))
    return x*10+y

# 输出数字 1484
print(reduce(fff,[1,4,8,4]))


# 字符串转换为数字
from functools import reduce
def fun(x,y):
    return x*10+y

def char2num(s):
    digits = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    return digits[s]

print(reduce(fun,map(char2num,"1208746")))


# -----------------------
# filter函数
# filter(def,Iterator),传入的函数返回一个bool值。
# 将Iterable每个元素都执行，如果为True保留，否则删除。即起到了过滤的作用

# 输出所有的奇数
def ffff(x):
    return x%2 == 1

r = filter(ffff,list(range(1,29)))

for n in r:
    print(n)

# ----------------------
# sorted函数
# 数字排序指定key进行排序，abs指 根据绝对值排序
sorted([36, 5, -12, 9, -21],key=abs)
# 字符串排序
sorted(['bob', 'about', 'Zoo', 'Credit'])# 根据ASCII的顺序排序
sorted(sorted(['bob', 'about', 'Zoo', 'Credit']),key=str.lower)# 忽略大小写排序,本质上是将key的方法作用于每一个元素。然后进行排序
sorted(sorted(['bob', 'about', 'Zoo', 'Credit']),key=str.lower,reverse=True)# 忽略大小写，并且反向排序

L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]
# 按成绩从高到低排序
def by_score(score):
    return -score[1]
# 按姓名忽略大小写倒序排序
def by_name(name):
    return name[0].lower()
# L2 = sorted(L,key=by_score)
# 也可以写匿名函数,按成绩从高到低排序
L2 = sorted(L,key=lambda x:-x[1])
print(L2)
# ----------------------
# 返回函数
# 注意：函数A返回一个函数B时,函数A的局部变量能在函数B中被引用；
def lazy_sum(*args,**kwargs):
    def sum():
        count = 0
        for i in args[0]:
            count+=i
        return count
    return sum
sum = lazy_sum([1,2,3,4])
print(sum())
# 注意：函数B并不立即执行，直到被调用时才执行
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())# 当被调用的时候 i 已经等于3 了。循环变量也是局部变量，所以尽量不要使用循环变量
print(f2())
print(f3())
# 如果一定要使用循环变量,可以再定义一个内部函数
def count1():
    def f(i):
        def g():
            return i*i
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))# 这里f()已经被调用了，所以参数可以传到g()中
    return fs
f4,f5,f6 = count1()
print(f4())
print(f5())
print(f6())
# 上面的方法count1可以写成
def count2():
    def f(i):
        return i*i
    fs = []
    for i in range(1,4):
        fs.append(lambda i: f(i))
    return fs
f4,f5,f6 = count2()
print(f4())
print(f5())
print(f6())

# 递增函数的实现，调用一次递增一次
def createCounter():
    global n
    def counter():
        nonlocal n
        n+=1
        return n 

    return counter

counter = createCounter()
print(counter(),counter(),counter())
# ----------------------
# 匿名函数 (重要)
f  = lambda i:i*i
print(f(5))
# 用于map中(map函数将可迭代的Iterable转换为迭代器Itertor)
print(map(lambda x: x*x,[1,2,3,4]))
# 用于filter 筛选list
L = list(filter(lambda n: n%2==0,range(1,5)))
print(L)
# 用于reduce
from functools import reduce
sum = (reduce(lambda x,y: x+y,range(1,101)))
print(sum)
# ----------------------
# 装饰器 (重要)
from datetime import datetime
# 普通装饰器
def log(func):
    def wrapper(*args,**kw):
        print(func.__name__)
        return func(*args,**kw)
    return wrapper


@log
def now():
    print(datetime.now())
# 调用方法
print(now.__name__)

# 带参数的装饰器
import functools
def log1(text):
    def decorator(func):
        @functools.wraps(func)# 有了这一步就省略了名字赋值
        def wrapper(*args,**kw):
            print(text,func.__name__)
            return func(*args,**kw)
        # wrapper.__name__ = func.__name__ # 这一步是为了now1的__name__始终是本身
        return wrapper
    return decorator

@log1('execute')
def now1():
    print('time is now.')
now1()  # 相当于 now = log(now),把now作为变量传递给装饰器，
print(now1.__name__)

# 打印方法执行时间
import time
import functools
from time import sleep

def print_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start = time.time()
        f = func(*args,**kw)
        end = time.time()
        print("%s executed in %.4f ms"%(func.__name__,end-start))
        return f
    return wrapper
@print_time
def test1():
    for i in range(0,1):
        sleep(1)
test1()

# 同时支持有参和无参的装饰器
def log2(arg):
    if isinstance(arg,str):
        # 参数是字符串
        def decorator(func):
            def wrapper(*args,**kw):
                print("arg is ",arg)
                return func(*args,**kw)
            return wrapper
        return decorator
    else:
        # 参数不是字符串
        def wrapper(*args,**kw):
                return arg(*args,**kw)
        return wrapper

@log2()
def test_log2():
    print('im working.')

test_log2()

# ----------------------
# 偏函数
# 声明一个函数，这个函数是另一个函数带指定参数的函数。
# 例子
i = int('A',base=16) # 将这个参数转换成10进制
print(i)
# 使用工具类
import functools

int2 = functools.partial(int,base=2)
print(int2('1000'))

max10 = functools.partial(max,10)
print(max10(1,2,35))