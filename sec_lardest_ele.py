arr=[int(x) for x in input("enter a element for array: ").split()]
first=sec=float('-inf')

for i in range(len(arr)):
    if arr[i]>first:
        sec=first
        first=arr[i]

    elif arr[i]>sec and arr[i]!=sec:
        sec=arr[i]

print("Secound largest element is: ",sec)