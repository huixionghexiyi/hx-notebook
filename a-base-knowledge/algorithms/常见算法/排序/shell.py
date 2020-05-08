'''
希尔排序
插入排序的升级版
'''
def shell(nums):
    n = len(nums)
    gap = n//2
    while gap:
        for i in range(gap,n):
            while i - gap >= 0 and nums[i-gap] > nums[i]:
                nums[i-gap],nums[i] =nums[i],nums[i-gap]
                i-=gap
        gap //=2

if __name__ =='__main__':
    a = [3,21,2,2,1,52]
    shell(a)
    print(a)