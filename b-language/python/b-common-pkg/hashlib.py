# 常见的摘要加密算法 MD5 SHA1等
'''
将一个长度固定的字符串，通过算法计算，输出一个固定长度的摘要值，如果源字符串被修改了1个bit，计算结果都会不同
又叫：哈希算法，散列算法
'''
# md5
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8')) #生成128bit，通常是一个32位16进制的字符串表示
print(md5.hexdigest())

# sha1
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8')) # 生成160bit，数据量大，也可以分批次update
print(sha1.hexdigest())

'''
sha256，sha512 更安全但是更慢。
原理是把 把无限多的数据集合映射到一个有限集合中
用途：用于加密密码。
'''