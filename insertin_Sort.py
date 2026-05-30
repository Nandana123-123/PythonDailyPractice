arr=[int(x) for x in input("Enter a numbers: ").split()]

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(key<arr[j] and j>=0):
        arr[j+1]=arr[j]
        j=j-1

    arr[j+1]=key

print(arr)