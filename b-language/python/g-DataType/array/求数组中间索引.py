'''
寻找第一个满足以下条件的索引：
该索引对应的数的左边和右边的和相等。
例子：
[1,2,0,1]  :: 1  索引1对应的数是2，左边之和等于右边之和
[2,3,5,4,1] :: 2
[0,0,0,1] :: 3
[1,3] :: -1  不存在这样的索引返回-1
'''
class Solution:
    def pivotIndex(self,nums):
        total = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i])*2+nums[i] == total:
                return i
        return -1