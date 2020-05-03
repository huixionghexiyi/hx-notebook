
'''
黑客在得到哈希值后，可以通过彩虹表来反推正确的密码。所以，在这个时候，再加上一个key，使得加密的内容位 message+key 的混合字符串，针对相同的message，不同的key会有不同的hash值
输入的值都是bytes
'''
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
h.hexdigest()
