num=[2,3,7,4,3,2,2]
d={}
for ele in num:
    d[ele]=d.get(ele,0)+1

res=[]
for k,v in d.items():
    if v==1:
        res.append(k)
print(res)