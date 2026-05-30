#method 1

def union(s):
    t=s.replace(" ","")
    seen=[]
    for ele in t:
        if ele in seen:
            return False
        else:
            seen.append(ele)
    return True


s=input("Enter a String: ")
u=union(s)
print(u)

#method 2

s=input("Enter a String: ")
dup=[]
for ele in s.replace(" ",""):
    if s.count(ele)>1:
        dup.append(ele)

if len(dup)!=0:
    print("False")

else:
    print("True")

