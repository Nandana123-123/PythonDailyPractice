def max_min(nums):
    lar=nums[0]
    small=nums[0]
    for i in range(len(nums)):
        if nums[i]>lar:
            lar=nums[0]

        if nums[i]<small:
            small=nums[i]

    print("largest: ",lar)
    print("smallest: ",small)\

nums=[int(x) for x in input("Enter a number: ").split()]
max_min(nums)