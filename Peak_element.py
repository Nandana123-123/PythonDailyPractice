def findPeakElement(nums):
        lar=nums[0]
        for ele in nums:
            if ele>lar:
                lar=ele

        for i in range(len(nums)):
            if nums[i]==lar:
                return i
            
arr=[int(x) for x in input("Enter a numbers for the array: ").split()]
print(findPeakElement(arr))