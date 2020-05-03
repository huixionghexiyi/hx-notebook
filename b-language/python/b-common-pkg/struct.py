# struct处理字节域其他二进制数据类型的转换。

import struct # linux下才能使用，或者pyhton终端里
b = struct.pack('>I',213124) # 第二个参数的个数要和前面一致
print(b)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80') # 一共有6个字节，所以使用IH，表示前4个用I参数，后2个用H参数。
'''
> 表示网络序
I 表示4字节无符号整数
H 表示2字节无符号整数
'''