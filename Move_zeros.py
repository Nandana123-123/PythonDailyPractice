def moveZeroes(nums):
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] != 0:
                res.append(nums[i])

        while len(res) < n:
            res.append(0)

        nums[:]=res
        return nums

nums=[int(x) for x in input("Enter a list of numbers: ").split()]
print(moveZeroes(nums))