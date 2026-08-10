n=1234
maxi=0
while n>0:
    rem=n%10
    if rem>maxi:
        maxi=rem

    n=n//10

print(maxi)