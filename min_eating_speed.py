import math

def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(float(pile) / mid)
            
        if total_hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
piles=[int(x) for x in input("Enter a piles: ").split()]
h=int(input("Enter a hours: "))
print(minEatingSpeed(piles,h))
