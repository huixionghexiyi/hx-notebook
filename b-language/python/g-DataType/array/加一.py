'''
修改list，满足以下条件：
1. 将list看成一个数字：[1,2,3] 等价于：23
2. 将这个数字+1 [1,2,3] => [1,2,4]
例：
[1,2,9] => [1,3,0]
[9,9] => [1,0,0]
'''


class Solution:
    def plusOne(self, digits):
        carr = 1
        i = len(digits) - 1
        while carr:
            digits[i] += carr
            if digits[i] > 9:
                digits[i] = digits[i] % 10
            else:
                carr = 0
            i -= 1
            if i < 0 and carr == 1:
                digits.insert(0, 1)
        return digits


s = Solution()
a = s.plusOne([9])
print(a)
