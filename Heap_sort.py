import heapq


arr=[int(x) for x in input("Enter a array elements: ").split()]
heapq.heapify(arr)
sor=[heapq.heappop(arr) for _ in range(len(arr))]
print(sor)


