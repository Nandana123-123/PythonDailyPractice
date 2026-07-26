def maximumProduct(nums):
    nums.sort()
    n=len(nums)
    p1=nums[0]*nums[1]*nums[n-1]
    p2=nums[n-1]*nums[n-2]*nums[n-3]

    return max(p1,p2)

nums=[int(x) for x in input("enter a element for an array: ").split()]
max_prod=maximumProduct(nums)
print(max_prod)

