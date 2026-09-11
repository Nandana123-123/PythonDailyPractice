import heapq

def maxSlidingWindow(nums, k):
    res = []
    heap = []

    for i in range(k):
        heapq.heappush(heap, (-nums[i], i))

    res.append(-heap[0][0])

    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))

        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        res.append(-heap[0][0])

    return res

nums=[int(x) for x in input("Enter a list of numbers: ").split()]
k=int(input("Enter a k value: "))
print(maxSlidingWindow(nums,k))