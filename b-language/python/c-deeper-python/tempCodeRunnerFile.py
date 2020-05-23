for i in [1,2,3]:
    print(i)

# Itertor 每调用一次next() ,返回一个元素
f = map(lambda i:i*i,[1,2,3])
next(f)