def flatten(n):
    res=[]
    for i in n:
        if isinstance(i,list):
            res+=flatten(i)
        else:
            res.append(i)

    return res



n=[5,7,8,9,[2,4],[6]]
print(flatten(n))
