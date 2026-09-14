s=input("Enter a string: ")
sub_s=input("Enter the substring to search for: ")
count=0
n=len(s)
m=len(sub_s)

for i in range(n-m+1):
    strs=s[i:i+m]
    if strs==sub_s:
        count+=1

print("the total number of substrings were: ",count)
