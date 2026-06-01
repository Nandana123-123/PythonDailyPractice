arr=[int(x) for x in input("Enter a array elements: ").split()]
rev=[]
for ele in arr:
    rev=[ele]+rev

print(rev)

#using built in functions

arr=[int(x) for x in input("Enter a array elements: ").split()]
print(arr[::-1])

#method 3
arr=[int(x) for x in input("Enter a array elements: ").split()]
rev=[]
for ele in range(len(arr)-1,-1,-1):
    rev.append(arr[ele])

print(rev)
