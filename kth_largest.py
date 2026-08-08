def findKthLargest(nums, k):
    nums.sort()
    return nums[len(nums)-k]

nums=[int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
k=int(input("Enter the value of k: "))
print(findKthLargest(nums, k))