def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i

    return len(nums)

nums=[int(x) for x in input("Enter a numbers: ").split()]
target=int(input("Enter a target: "))
print(searchInsert(nums,target))
        