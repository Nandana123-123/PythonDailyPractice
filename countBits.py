def countBits(n):
        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i//2]+(i%2)
        return ans

n=int(input("Enter a number: "))
print(countBits(n))