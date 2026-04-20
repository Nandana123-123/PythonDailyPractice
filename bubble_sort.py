arr=[3,6,80,11,23,56]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)