import re
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)') # 使用前瞻和回顾，保证电话前后不应该出现数字。
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。
'''
res = re.findall(pattern,sentence) # 返回一个List
re.purge()
res = pattern.findall(sentence) # 与上面个等价
print('='*4+'findall结果'+'='*4)
print(res)
for r in res:
    print(r)
# finditer
res_iter = pattern.finditer(sentence) # 返回一个可迭代对象
print('='*4+'finditer结果'+'='*4)
print(res_iter)
for i in res_iter:
    print(type(i))
    print(i.group())