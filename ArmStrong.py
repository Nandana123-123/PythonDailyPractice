num=int(input("Enter a number: "))
temp=num
n=len(str(num))
total=0

while temp>0:
    rem=temp%10
    total+=rem**n
    temp//=10

if(total==num):
    print(num," is a armstrong number")
else:
    print(num, " is not a armstrong number")