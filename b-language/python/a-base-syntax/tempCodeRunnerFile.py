from functools import reduce

def fff(x,y):
    # print(str(x)+"==="+str(y))
    return x*10+y

# 输出数字 1484
print(reduce(fff,[1,4,8,4]))