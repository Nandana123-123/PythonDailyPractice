#to check a prime number in a range
n=int(input("Enter a number: "))
for i in range(2,n):
    for j in range(2,int(n**0.5)+1):
        if i == 2 or i == 1:
            print(i, "prime")
            break
        if(i%j)==0:
            print(i,"not a prime")
            break
        else:
            print(i,"prime")

#to check wheather a given number is prime or not

n=int(input("Enter a number: "))
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(n,"not prime")
        break
else:
    print(n,"prime")

