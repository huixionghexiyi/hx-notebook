# 函数，帮助我们少写重复的代码。
# 官方文档：
# http://docs.python.org/3/library/functions.html#abs
import test
abs(-100)# 取绝对值
max(1,4,10,-1,4) # 取最大值

#类型转换
int('123') # str转int
float('12,34') # str转float
str(1.23) # float转str
bool(1) # int 转bool true
bool('') # str转bool flase
a = abs # 相当于给abs取了一个别名,或变量a指向abs函数
print(a(-10))

print(hex(100)) # 把一个整数转换成十六进制表示的字符串

# 自定义函数

def my_abs(a):
    if a<0:
        return -a
    else :
        return a

print(my_abs(-10))

# 然后就是，我们可以用各种递归等思想设计我们的函数




