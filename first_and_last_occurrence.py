def searchRange(nums, target):
    def find(first):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                ans = mid
                if first:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return ans

    return [find(True), find(False)]


nums=[int(x) for x in input("Enter the elements of the sorted array separated by spaces: ").split()]
target=int(input("Enter the target value to search for: "))
print(searchRange(nums, target))
