# -*- coding: utf-8 -*-
###################
# 编码问题
# 链接： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
print('hello 世界')
print(ord('中'))
print(chr(25991))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
#一个2表示占2位，02 表示占两位，且第一位是0
print('%2d-%02d' % (3, 1))
#表示小数点后面取两位
print('%.3f' % 3.1415926)
# 输出多行
print('''
# nice
?
?
?
''')
# 输入 input
a = input('fuck:')
print(input(a))

# list一种有序的、可变的集合，可以随时添加或删除其中的元素。
classmate = [1,2,'fuck']
print(classmate)
print(classmate[0])
# print(classmate[3])数组下标溢出错误
print(classmate[-1])# 倒叙输出  
len(classmate) # 显示list的长度
classmate.append('tail')# 追加到末尾
classmate.insert(1,'test') # 插入到指定位置
print(classmate)# 测试一下
classmate.pop() #弹出末尾的元素 ，这里相当于栈
classmate.pop(1)# 删除指定位置的元素
# classmate.sort()# 排序,当list中都是数字或str时才可以排序



# tuple 元组，一旦初始化就不能修改。

myTuple = ('t1','t2','t3',) #可以加 `,` 如果tuple中只有一个元素时必须加`,`  这是为了避免歧义
singleTuple=(2,) #加上`,`才是元组，不然就是整数 2 
myTuple[0]
#没有insert 和append方法 其他的和list一样

# 条件判断

age = 20
# python中的缩减还是比较严格的，毕竟没有{} 注意if  和else后要用 :  连接条件句
if age >= 18:
    print("your age is ",age)
    
else:
    print('why u so young')
    print('part 2')
# 使用elif的条件句
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 需要注意的是：
# 当使用input输入的时候，输入的默认是 str 类型。需要转换成 int才能比较。不然会报错。
# 转换之后输入 'abc' 也会报错。因为'abc'不能转换成 int 

x = input('age:') # 输入会报错，因为是str类型 不能和 18 比较
age = x;# 需要转换从 age = int(x)，同时不能输入 'abc'
if age >= 18:
    print("your age is ",age)
else :
    print('too young')

# 循环
# 记得要加  `:`
# 本质是将集合中的数据每个都顺序处理一遍
names = ['a','b','c']
for name in names:
    print(name)

list(range(100)) # 生成从 0 到 99 的整数序列。

sum = 0
for x in range(100):
    sum = sum+x
print(sum)

# while 循环

sum = 0 
n = 99
while n>0:
    sum += n
    n-=2
print(sum)

# 循环的其他关键字
# break 提前结束循环
# continue 跳过当前的这次循环，进入下一次循环

#再次强调，注意缩进。

# dict  具有存储的是键值，极快的查找速度，浪费内存多（底层是通过hash算法计算存储位置）
# 而list相反，查找、插入的时间随元素的增加而增加。内存占用小

d={'a':10,'b':14,'c':17} # 定义一个字典
print(d['a'])
# 修改与创建
d['a'] = 11 # 如果存在就是修改
d['d'] = 22 # 如果不存在就是添加
print(d['d'])

# 判断 某个元素是否在集合中
if('d' in d) :
    print('yes')

d.get('c') # 如果存在key，返回value，如果不存在返回None
d.get('e',10) # 如果存在返回value，如果不存在返回10
d.pop('b') # 删除一个键值对

# set集合,可以看成是一个不存储value值的dict

s = set([1,2,3])
s.add(10)# 添加元素到set，重复元素会被忽略
s.remove(10)# 移除y元素 

# 不可变性
# 在一个str中
st = "adb"
st1 = st.replace('a','A')# 修改a为A
print(st1)
print(st)
# 需要注意的是，本质上并不是修改了'a',而是创建了一个新的"Adb",再让st指向它

# 小结：对于不变对象来说，调用对象自身的任何方法都不会改变对象自身的内容
# 相反这些方法会创建新的对象并返回


