def getMaxOccuringChar(s):
    f={}
    for ele in s:
        f[ele]=f.get(ele,0)+1
        
    maxi=max(f.values())
    for k,v in sorted(f.items()):
        if maxi==v:
            return k
    return '$'

s=input("Enter a sentence: ")
print(getMaxOccuringChar(s))