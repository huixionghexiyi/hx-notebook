'''
基数排序
'''


def radix_sort(nums):
    if not nums:
        return nums
    _max = max(nums)
    maxDigit = len(str(_max))
    div, mod = 1, 10
    buckets = [[] for i in range(10)]
    for i in range(maxDigit):
        for num in nums:
            buckets[num % mod//div].append(num)
        index = 0
        for j in range(10):
            for item in buckets[j]:
                nums[index] = item
                index += 1
            buckets[j] = []
        div, mod = div*10, mod*10

if __name__ == "__main__":
    a = [3,-1]
    radix_sort(a)
    print(a)