def majority(nums):
    nums.sort()
    n=len(nums)
    for i in range(n):
        if nums[i]==nums[n//2]:
            return nums[i]

    return -1

nums=[int(x) for x in input("enter a element for an array: ").split()]
maj=majority(nums)
print(maj)
