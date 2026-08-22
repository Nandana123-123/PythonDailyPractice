def findMaxAverage(nums, k):
    summ=0
    for i in range(k):
        summ+=nums[i]

    cur=summ
    for i in range(k,len(nums)):
        summ=summ+nums[i]-nums[i-k]
        if summ>cur:
            cur=summ   
    return cur/float(k)

nums=[int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
k=int(input("Enter a number: "))
print(findMaxAverage(nums,k))