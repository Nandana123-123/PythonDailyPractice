def hammingWeight(n):
    count=0
    while(n>0):
        if (n&1)==1:
            count+=1
        n=n>>1
    return count

n=int(input("enter a number: "))
print(hammingWeight(n))