def Factorial(n):
    if n==0:
        return 1
    return n*Factorial(n-1)

n=int(input("Enter a number: "))
print(Factorial(n))

#method 2

n=int(input("Enter a number: "))
i=1
fact=1
while(n>=i):
    fact*=i
    i+=1
print("factorial :",fact)


