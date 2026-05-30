def common_ele(a,b,c):
    cmn=[]
    for i in a:
        for j in b:
            for k in c:
                if i==j==k:
                    cmn.append(i)
    return sorted(cmn)

a=[int(x) for x in input("Enter a array elements: ").split()]
b=[int(x) for x in input("Enter a array elements: ").split()]
c=[int(x) for x in input("Enter a array elements: ").split()]
res=common_ele(a,b,c)
print(res)


#using set operation like intersection

def common_ele(a,b,c):
    set_a=set(a)
    set_b=set(b)
    set_c=set(c)

    cmn=set_a.intersection(set_b).intersection(set_c)
    res=list(sorted(cmn))
    return res

a=[int(x) for x in input("Enter a array elements: ").split()]
b=[int(x) for x in input("Enter a array elements: ").split()]
c=[int(x) for x in input("Enter a array elements: ").split()]
res=common_ele(a,b,c)
print(res)

