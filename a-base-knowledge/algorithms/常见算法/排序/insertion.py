'''
插入排序
'''


def insertion(nums):
    n = len(nums)
    for i in range(n):
        while i > 0 and nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1

if __name__ == '__main__':
    a = [2, 4, 5, 1, 24, 1, 2]
    insertion(a)
    print(a)
