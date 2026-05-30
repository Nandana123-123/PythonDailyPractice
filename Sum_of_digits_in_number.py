n=int(input("Enter a number: "))
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n//=10

print("sum of ",temp," is ",sum)


