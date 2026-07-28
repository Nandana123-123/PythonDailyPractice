def sortColors(nums):
    low=0
    mid=0
    high=len(nums)-1
    while(mid<=high):
        if nums[mid]==0:
            temp=nums[mid]
            nums[mid]=nums[low]
            nums[low]=temp
            low+=1
            mid+=1

        elif nums[mid]==1:
            mid+=1

        else:
            temp=nums[mid]
            nums[mid]=nums[high]
            nums[high]=temp
            high-=1


nums=[int(x) for x in input("enter a element for an array: ").split()]
sortColors(nums)
print(nums)