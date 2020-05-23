'''
快速排序
基本原理：
选择一个数作为锚点，让锚点左边的数小于他，让锚点右边的数大于他。
然后将左右两边的数同样选择一个锚点，做同样的操作。
平均复杂度：nlogn
'''


def quick(nums, l, r):
    '''
    递归实现
    '''
    if r-l <= 0:
        return
    mid = partition(nums, l, r)
    quick(nums, l, mid-1)
    quick(nums, mid+1, r)


def partition(nums, l, r):
    i = l-1
    for j in range(l, r):
        if nums[j] < nums[r]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def quick_loop(nums, left, right):
    '''
    迭代实现
    '''
    if left >= right:
        return nums
    pivot = left
    i = left
    j = right
    while i < j:
        while i < j and nums[j] > nums[pivot]:
            j -= 1
        while i < j and nums[i] <= nums[pivot]:
            i += 1
        nums[i],nums[j]=nums[j],nums[i]
    nums[i],nums[pivot] = nums[pivot],nums[i]
    quick_loop(nums,left,j-1)
    quick_loop(nums,j+1,right)
    return nums

if __name__ == '__main__':
    a = [1, 2, 5132, 1, 4, 214, 5, 66]
    quick(a, 0, len(a)-1)
    # quick_loop(a,0,len(a)-1)
    print(a)
