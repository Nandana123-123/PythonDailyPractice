def singleNonDuplicate(nums):
    res=0
    for i in range(len(nums)):
        res=res^nums[i]

    return res

nums=[int(x) for x in input("Enter a numbers: ").split()]
print(singleNonDuplicate(nums))