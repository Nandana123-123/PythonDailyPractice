def longestConsecutive(nums):
    n=len(nums)
    if n==0:
        return 0
    nums.sort()
    count=1
    maxCount=1

    for i in range(1,n):
        if nums[i]==nums[i-1]:
            continue

        if nums[i]==nums[i-1]+1:
            count+=1
        else:
            count=1

        if count>maxCount:
            maxCount=count

    return maxCount


nums=[int(x) for x in input("Enter a numbers for an array: ").split()]
print(longestConsecutive(nums))

