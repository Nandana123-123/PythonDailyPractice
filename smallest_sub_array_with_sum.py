def SmallesSubArraySum(arr,x):
    n=len(arr)
    min_sum=len(arr)+1
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]

            if(sum>x):
                if j-i+1<min_sum:
                    min_sum=j-i+1
                break

    if min_sum>n:
        return 0
    return min_sum

arr=[int(x) for x in input("Enter a number for array: ").split()]
x=int(input("Enter a value for x: "))
print(SmallesSubArraySum(arr,x))