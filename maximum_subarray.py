def maxSubArray(nums):
    cur=nums[0]
    maxi=nums[0]
    num=[nums[0]]
    for i in range(1,len(nums)):
        cur=max(nums[i],nums[i]+cur)
        
        if cur>maxi:
            maxi=cur
            num.append(nums[i])
    print(num)
    return maxi

nums=[int(x) for x in input("Enter a numbers for an array: ").split()]
print(maxSubArray(nums))
