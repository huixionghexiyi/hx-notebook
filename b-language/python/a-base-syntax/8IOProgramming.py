"""
- 查看下面连接，编写笔记
https://www.liaoxuefeng.com/wiki/1016959663602400/1017606916795776
"""

# 通常操作系统是不允许普通程序直接操作磁盘的。
# 所以，读写文件就是请求操作系统打开一个文件对象。然后操作系统提供的接口从这个文件中读写数据。

#------------------
# 读文件
# 获取一个文件对象
# -*- coding: utf-8 -*-
f = open("C:/Users/huixiong/Desktop/test.txt",'r')
# f = open("C:/Users/huixiong/Desktop/test.txt",'r',encoding='utf-8') # 使用utf-8编码
# f = open("C:/Users/huixiong/Desktop/test.txt",'r',encoding='utf-8'，error='igonre') # 使用utf-8编码，error=忽略错误
#读取文件内容
p = f.read()
print(p)
# 如果文件出错，下面方法就不会调用，在程序结束前都不会释放资源。所以最好还是try..finally
f.close()

try:
    f = open("C:/Users/huixiong/Desktop/test.txt",'r')
except IOError as e:
    print("read error:%s"% e)
finally:
    f.close()# 关闭文件对象

# 但是像上面这样写会很麻烦引入with

with open('C:/Users/huixiong/Desktop/test.txt') as f:
    print(f.read())

## 注意：调用read时，是将文件全部加载到内存当中。如果文件太大。内存会溢出。
f.read(100)# 读取100字节
f.readline()# 读取一行
f.readlines()# 读取所有，按行返回到一个list中

## 文件小，使用read()；文件大，read(size)安全。配置文件，readlines()方便，并且使用line.strip()去掉'\n'


"""
# file-like Object 
# 类似于open()返回的对象，并且带有read()方法。统称为file-like Object。包括：file、内存字节流、网络流、自定义流
## StringIO是在内存中创建的file-like Object 常作为l临时缓冲。
"""

#------------------
# 二进制文件
f = open('C:/Users/huixiong/Desktop/test.jpg','rb')# utf-8的编码可以直接这样读取
print(f.read())# 读取到的是16进制

# 其他编码需要写encoding,忽略编码中的错误和不规范写errors='ignore'
f = open('C:/Users/huixiong/Desktop/test.jpg','r',encoding='gbk',errors='ignore')


#--------------
# 写文件
f = open('C:/Users/huixiong/Desktop/test.txt','a')# w 表示写，wb表示写二进制，a 表示追加到后面
f.write("\nHello World!")# 这里会覆盖
f.close()

#-------------------
# StringIO和BytesIO

# 想把str写入StringIO,需要创建一个StringIO对象。
from io import StringIO
f = StringIO()
f = StringIO("Hello\nWorld!")#初始化
f.write("hello")# 写入到内存,返回写入字符的数量，这里返回5
f.write(" ")# 写入空格。
f.write("world!")
f.getvalue() # 获取f对象的值，这里返回: hello world!
f.readline()# 读取一行

#------------------
# BytesIO
from io import BytesIO
f = BytesIO()# 童颜哥也是在内存中，读写bytes
f.write("中文".encode("utf-8"))# 中文一个字符是3个字节。所以返回 6
print(f.getvalue())# 返回16进制

#-------------------
# 操作文件和目录
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088