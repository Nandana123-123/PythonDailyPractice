def maxProduct(nums):
    n=len(nums)
    maxi=nums[0]
    mini=nums[0]
    res=nums[0]
    for i in range(1,n):
        if nums[i]<0:
            temp=maxi
            maxi=mini
            mini=temp

        maxi=max(nums[i],maxi*nums[i])
        mini=min(nums[i],mini*nums[i])

        if(maxi>res):
            res=maxi

    return res

nums=[int(x) for x in input("Enter a numbers for an array: ").split()]
print(maxProduct(nums))
