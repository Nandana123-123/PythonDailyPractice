def twoSum(nums, target):
        lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    lst.append(i)
                    lst.append(j)

        return lst

nums=[int(x) for x in input("Enter a numbers for list: ").split()]
target=int(input("Enter a target element:"))
print(twoSum(nums,target))