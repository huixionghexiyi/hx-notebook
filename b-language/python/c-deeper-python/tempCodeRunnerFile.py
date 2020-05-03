s = [1, 2, 3]
x = 3
i, j = 1, 3
len(s)  # 长度
min(s)  # 序列中的最小元素，s中元素需要可比较
max(s)  # 序列中的最大值，s中元素需要可比较
s.index(x, i, j)  # 返回从i到j位置第一次出现x的位置
print(s.count(x))