arr=[int(x) for x in input("Enter a array elements: ").split()]

for i in range(len(arr)-1):
    min_indx=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_indx]:
            min_indx=j

    arr[i],arr[min_indx]=arr[min_indx],arr[i]

print(arr)