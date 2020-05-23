'''
归并排序
平均时间复杂度： nlogn
'''


def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i == len(left):
        res += right[j:]
    else:
        res += left[i:]
    return res


if __name__ == "__main__":
    a = [5, 12, 2, 1, 22]
    a = merge_sort(a)
    print(a)
