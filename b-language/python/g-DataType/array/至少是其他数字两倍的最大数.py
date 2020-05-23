'''
求索引，满足以下条件：
1. 索引对应的数字至少是其他数字的2倍

[1,6,3] # 1
[1,2,3] # -1
[1,8,8] # 1
[1] # 0
[0,1] # 1
'''


class Solution:
    def dominantIndex(self, nums):
        large = 0
        sec = 0
        ind = 0
        for i in range(len(nums)):
            if nums[i] > large:
                sec = large
                large = nums[i]
                ind = i
            elif nums[i] > sec and nums[i] != large:
                sec = nums[i]
        return ind if large >= sec*2 else -1
