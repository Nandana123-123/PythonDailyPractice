sen=input("Enter a string: ")
res=""
for ele in sen:
    if ele==" ":
        res+='!'
    else:
        res+=ele
print(res)