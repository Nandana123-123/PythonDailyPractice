def subsets(nums):
    res = [[]]

    for i in range(len(nums)):
        n = len(res)

        for j in range(n):
            new = res[j].copy()
            new.append(nums[i])
            res.append(new)

    return res


nums = [1,2,3]
print(subsets(nums))