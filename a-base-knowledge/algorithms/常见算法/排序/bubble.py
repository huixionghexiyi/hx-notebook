'''
冒泡排序
'''
def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1,n-i):
            if nums[j]<=nums[j-1]:
                nums[j-1],nums[j]=nums[j],nums[j-1]

if __name__ == '__main__':
    a = [24,12,1,35,22,55,1]
    bubble(a)
    print(a)