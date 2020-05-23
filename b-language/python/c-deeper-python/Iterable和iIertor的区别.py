# https://www.cnblogs.com/meditator/p/7943582.html

#python中的tunple,list,dict,str是可迭代的(Iterable),不是迭代器(Itertor)。
#Iterable是实实在在的占用内存的,其中的每个元素都存在于内存中。

# Iterable的循环
# Iterable不能使用next(),猜测是因为for底层是将Iterable转换成了Itertor。所以Itertor可以使用for,而Iterable不能使用next()
for i in [1,2,3]:
    print(i)

# Itertor 每调用一次next() ,返回一个元素
f = map(lambda i:i*i,[1,2,3])
next(f)
# for 底层是用next。所以，可以使用for
for i in f:
    print(i)

# 将Iterable转换成一个Itertor
f = iter([1,2,3,4])
# map生成一个Itertor
f = map(lambda i:i,[1,2,3,4])

