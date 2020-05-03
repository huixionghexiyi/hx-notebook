def selection(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]

if __name__ =='__main__':
    a = [12,4,5,2,5,1]
    selection(a)
    print(a)