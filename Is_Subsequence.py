t=input("Enter a main string: ")
s=input("Enter a Sub sequence string: ")
i=0
for ele in t:
    if i<len(s) and ele==s[i]:
        i+=1

if(i==len(s)):
    print("Subsequence found")
else:
    print("Subsequence not found")