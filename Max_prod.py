def maxProduct(nums):
    n=len(nums)
    cur_max=0
    maxi=0
    for i in range(n):
        for j in range(i+1,n):
            cur_max=max((nums[i]-1)*(nums[j]-1),cur_max)
            maxi=max(cur_max,maxi)

    return maxi


nums=[int(x) for x in input("enter a element for an array: ").split()]
max_prod=maxProduct(nums)
print(max_prod)