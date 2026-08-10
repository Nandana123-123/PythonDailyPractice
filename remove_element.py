def removeElement(nums, val):
    j=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[j]=nums[i]
            j+=1
    
    return j

nums=[int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
val=int(input("Enter a element to remove: "))
print(removeElement(nums,val))