#without using builtin function

def Merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        Merge_sort(left)
        Merge_sort(right)


        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1

            else:
                arr[k]=right[j]
                j+=1

            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1


arr=[int(x) for x in input("Enter a array elements: ").split()]
Merge_sort(arr)
print(arr)

#simplest one using reccursive logic

def MergeSort(arr):
    if(len(arr)<=1):
        return arr

    mid=len(arr)//2
    left=MergeSort(arr[:mid])
    right=MergeSort(arr[mid:])

    return sorted(left+right)

arr=[int(x) for x in input("Enter a array elements: ").split()]
sor=MergeSort(arr)
print(sor)



