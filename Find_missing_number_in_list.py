nums=[int(x) for x in input("Enter a number: ").split()]
full=range(min(nums),max(nums))
missing=set(full)-set(nums)
print(missing)