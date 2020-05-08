'''
桶排序
'''


def bucket_sort(nums, bucketSize):  # BucketSize 桶的大小
    if len(nums) < 2:
        return nums
    _max = max(nums)
    _min = min(nums)
    bucketNum = (_max - _min)//bucketSize + 1  # 桶的数量
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        buckets[(num - _min) // bucketSize].append(num)
    res = []
    for bucket in buckets:
        if not bucket:
            continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res


def bucket_sort1(nums, bucketSize):
    if len(nums) < 2:
        return nums
    _max = max(nums)
    _min = min(nums)
    bucketsNum = (_max - _min)//bucketSize + 1
    buckets = [[] for _ in range(bucketsNum)]
    for num in nums:
        buckets[(num-_min)//bucketSize].append(num)
    res = []

    for bucket in buckets:
        if not bucket:
            continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            if bucketsNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort1(bucket,bucketSize))
    return res


if __name__ == "__main__":
    a = [1, 24, 3, 2, 5, 6, 2, 5, 3, 5, 6, 6, 66]
    bucketSize = 3
    a = bucket_sort(a, bucketSize)
    print(a)
