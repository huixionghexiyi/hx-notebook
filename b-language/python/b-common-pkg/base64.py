# 可以将任意二进制文件：jpg、exe、pdf等转换为文本文件。可直接显示。

'''
原理：
提前准备包含64个字符的数组：['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
在计算机中：
1个字节 8 bit
3个字节一组，就是24bit
编码过程：
将24bit划分为4组，每组就6bit
6bit即6位，最多表示63
这样，每一个字节，对应字符数组中的一个字符。
如果不是3的倍数，则用\x00字节加在最后，再在编码上添加1或2个 = 号
'''
import base64
print(base64.b64encode(b'huixiong'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
base64.url

'''
URL、cookie中如果存在 = 会产生歧义
URL中使用 + /的编码字符串也可能产生歧义，所以使用urlsafe_encode() 换成 - 和 _
'''
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff') # 这里正常编码会出现 +和/
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') # 替换+和/为-和_
base64.urlsafe_b64decode('abcd--__') # 将-和_ 识别成+和/
