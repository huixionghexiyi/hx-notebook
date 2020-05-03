def func(*args, **kwargs):
    for i in args:
        print(i)
    print("="*10)
    for k, v in kwargs.items():
        print(k, v)


func(1, 2, 3)

with open("D:\\Projects\\HuixiongNote\\Python\\面试题.py", 'r',encoding='utf8' ) as file:
    data = file.read()
    print(data)


re = [y for y in map(lambda x:x*x,[x for x in range(1,6)]) if y >10]
print(re)

import random
a = random.randint(1,4)
b = random.random()
print(b)

import re
s = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>',s)
print(res)


a = 3
assert(a>2)
print("完事儿")

print(id(a))

s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
s = "".join(s)
print(s)

dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

lis = sorted(dic.items(),key=lambda i:[0],reverse=False)
print(lis)
print(dic.items())

import re
a = "not 404 found 张三 99 深圳"
lis = a.split(" ")
res = re.findall(r'\d+|[a-zA-Z]+',a)
new_str = " ".join([i for i in lis if i not in res])
print(new_str)

a = filter(lambda x:x%2 != 0,list(range(1,11)))
print(next(a))

l1 = [1,3,5,7]
l2 = [2,4,6,8]

# l1.extend(l2)
# l1 +=l2
# l1.append(l2)
print(l1)

a = [[1,2],[3,4],[5,6]]
print([j  for i in a for j in i])


a = [1,3,4]
b = [2]
print([i for i in zip(a,b)])
print(b"\xe4\xbd\xa0\xe5\xa5\xbd".decode())

import re
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
res = re.findall(r"dateRange=(.*?)%7C(.*?)&dateType",url)
print(res)

lis=[2,3,5,4,2,2,9,6]
new_list = []
def add(lis):
    a = min(lis)
    lis.remove(a)
    new_list.append(a)
    if len(lis) >0:
        add(lis)
    return new_list
new_list = add(lis)
print(new_list)

class Singleton(object):
    __instance = None
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(2,"dog")
b = Singleton(3,"dog")
print(id(a))
print(id(b))


a = "%.02f"%0.129123
print(a)

print(any(range(0,10)))
print(all(range(0,10)))

import copy
a = ["奈斯",[1,2,3,4]]
b = a
c = copy.copy(a)
# c[1] = ['a','b','c','d']
a[1][0] = 'a'
d = copy.deepcopy(a)
d[1] = ['a','b','c','d']
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:(x<0,abs(x)))
print(a)

foo = [("zs",19),("ll",54),("wa",17),("df",17)]
a = sorted(foo,key=lambda x:(x[1]))
a = sorted(foo,key=lambda x:(x[1],x[0]))
print(a)

a=['123213','qwf','q','2']
print(sorted(a,key= lambda x:len(x)))

import re
s="info:xiaoZhang 33 shandong"
res = re.split(r":| ",s)
res2 = s.split(" ")
print(res,res2) 

import re
email_lis = ["affff@163.com","b@163.email",'com.xiaobi@qq.com','c@163.com']
for e in email_lis:
    res = re.match(r'[\w]{4,20}@163\.com$',e)
    if res:
        print(e,res.group())
    else:
        print("not:"+e)

def get_sum(lis):
    if lis:
        res = lis.pop(0) + get_sum(lis)
    else:
        res = 0
    return res
res = get_sum(list(range(0,11)))
print(res)

import json
dic = {1:'a',2:'b',3:'c'}
a = json.dumps(dic)
b = json.loads(a)
print(type(a),type(b))

s = '   qwfwq wqfwq  wqf qwf  wqf '
print("".join(s.split(" ")))


import re
ret = re.match(r"1\d{9}[0-3,5-6,8-9]$","111111111114")
if ret:
    print(ret.group())

import re
title = "你好，hello， 狗屁"
pattern = re.compile(r'[\u4e00-\u9fa5]+')
print(pattern.findall(title))

import re
labels = "<html><h1>http://www.itcast.cn</h1></html>"
ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>",labels)
print(ret.group())

a = [1,2,3,3,3]
b = [2,3,4]
c = list(set(a).intersection(set(b))) # 交集
d = list(set(a).union(set(b))) # 并集
e = list(set(a).difference(set(b))) # 补集
print(c)
print(d)
print(e)

import random
res1 = 100*random.random()
res2 = random.choice(range(1,101))
res3 = random.randint(1,100)
print(res1)
print(res2)
print(res3)

import re
s  = "小明年龄28 工资180万"
res = re.search(r"\d+",s).group()
res2 = re.findall(r"\d+",s)
res3 = re.match(r"小明",s).group()
print(res)
print(res2)
print(res3)
a = ['123','12.123']
print(float(a[1]))

print({}.fromkeys(range(len("abcdefg")),0))
print(list(range(5)))

a = [1,2,3214,15,43,73,1]
s = []
for i in map(str,a):
    s.append(i)
print(s)

a = [0,0,0,0]
b = map(str,a) 
print(''.join(b).lstrip('0') or '0')

k = lambda x,y:x+y>y+x
print(k('2','3'))

class Solution:
  def isUnique(self, astr: str) -> bool:
    mark = 0
    for char in astr:
      move_bit = ord(char) - ord('a')
      if (mark & (1 << move_bit)) != 0:
        return False
      else:
        mark |= (1 << move_bit)
    return True

print(1<<(ord('l')-97))

print(4^1)

from threading import *
class Foo:
    def __init__(self):
        self.s1 = Semaphore(1)
        self.s2 = Semaphore(0)
        self.s3 = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.s1.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        print("one")
        self.s1.release()
        self.s2.acquire()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        print("two")
        self.s2.release()
        self.s3.acquire()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        print("three")
        self.s3.release()
