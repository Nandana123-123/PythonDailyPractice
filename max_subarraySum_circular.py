def maxSubarraySumCircular(nums):
    curmax=nums[0]
    maxres=nums[0]

    curmin=nums[0]
    minres=nums[0]

    total=nums[0]
    for i in range(1,len(nums)):
        if curmax<0:
            curmax=nums[i]
        else:
            curmax+=nums[i]
        if curmax>maxres:
            maxres=curmax

        if curmin>0:
            curmin=nums[i]
        else:
            curmin+=nums[i]

        if curmin<minres:
            minres=curmin

        total+=nums[i]

    if maxres<0:
        return maxres

    circular=total-minres
    
    return max(circular,maxres)

nums=[int(x) for x in input("Enter a numbers for an array: ").split()]
print(maxSubarraySumCircular(nums))