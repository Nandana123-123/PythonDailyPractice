def pairs(spells,potions,sucess):
    potions.sort()
    res=[]
    n=len(spells)
    m=len(potions)
    for i in range(n):
        left=0
        right=m-1
        pos=m
        while(left<=right):
            mid=left+(right-left)//2
            mul=spells[i]*potions[mid]
            if mul>=sucess:
                pos=mid
                right=mid-1
            else:
                left=mid+1

        res.append(m-pos)
    return res

sp=[int(x) for x in input("Enter for spells: ").split()]
po=[int(x) for x in input("Enter for potions: ").split()]
sucess=int(input("Enter for sucess: "))
print(pairs(sp,po,sucess))
