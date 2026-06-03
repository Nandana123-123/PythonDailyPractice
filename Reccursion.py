n=int(input("Enter a number: "))
print("Printing of first n numbers")
def recursion(n):
    if n==0:
        return 
    recursion(n-1)
    print(n)

recursion(n)

#method 2
print("factorial")
def  recurssionfact(n):
    if n==0:
        return 1
    return n*recurssionfact(n-1)
print(recurssionfact(n))


#method 3
print("fibinocii sequence")
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(n):
    print(fib(i))