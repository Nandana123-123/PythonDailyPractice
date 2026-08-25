def maxi(arr):
    mimi=arr[0]
    for ele in arr:
        if ele<mimi:
            mimi=ele
    print(mimi)

arr=[int(x) for x in input("Enter a number: ").split()]
maxi(arr)