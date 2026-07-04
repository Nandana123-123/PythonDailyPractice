def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    seen = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count

nums=[int(x) for x in input("Enter a numbers for a list: ").split()]
k=int(input("Enter the target sum: "))
print(subarraySum(nums, k))