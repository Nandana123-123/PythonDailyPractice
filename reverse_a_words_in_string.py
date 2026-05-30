#method 1

sen=input("Enter a string: ")
sp=sen.split()
rev=sp[::-1]
print(" ".join(rev))


#method 2

sen=input("Enter a string: ")
rev=" "
for ele in sen.split():
     rev=ele+" "+rev


print(rev)
