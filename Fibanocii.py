n=int(input("Enter a number: "))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b

#method 2

n=int(input("Enter a number: "))
a=0
b=1
while(a<=n):
    print(a)
    a,b=b,a+b

#method 3: using recursion

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=int(input("Enter a number: "))
print("Fibinocii sequence is: ")
for i in range(n):
    print(fib(i))