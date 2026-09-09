def isDisarium(n):
    sq=0
    temp=n
    temp1=n
    count=0
    while n>0:
        n=n//10
        count+=1
        

    while temp1>0:
        rem=temp1%10
        sq=(rem**count)+sq
        count-=1
        temp1=temp1//10
        
    if temp==sq:
        return True
    return False

n=int(input("Enter a number: "))
if isDisarium(n):
    print(f"{n} is disarium number")
else:
    print(f"{n} is not a disarium number")
