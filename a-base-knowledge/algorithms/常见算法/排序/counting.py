'''
计数排序
'''


def counting(nums):
    if not nums:
        return nums
    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    arr_tmp = [0]*(_max-_min + 1)
    for num in nums:
        arr_tmp[num - _min] += 1
    j = 0
    for i in range(n):
        while arr_tmp[j] == 0:
            j += 1
        nums[i] = j + _min
        arr_tmp[j] -= 1


if __name__ == "__main__":
    a = [1, 2, 4, 2, -54, 3]
    counting(a)
    print(a)
