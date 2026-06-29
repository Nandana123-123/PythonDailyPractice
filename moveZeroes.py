def moveZeroes(nums):
        num=[]
        for i in range(len(nums)):
            if nums[i]!=0:
               num.append(nums[i])
        while(len(num)<len(nums)):
            num.append(0)

        nums[:]=num

nums=[int(x) for x in input("Enter a numbers for a list: ").split()]
moveZeroes(nums)
print(nums)