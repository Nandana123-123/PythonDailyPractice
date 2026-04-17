def binary(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[int(x) for x in input("Enter a list of numbers: ").split()]
target=int(input("Enter a target: "))
bin=binary(arr,target)

if(bin):
    print("found at index ",bin)
else:
    print("not found")