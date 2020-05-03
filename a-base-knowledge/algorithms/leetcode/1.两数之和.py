#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            r = target - num
            if r in nums and i != nums.index(r):
                return [i, nums.index(r)]
        # @lc code=end
