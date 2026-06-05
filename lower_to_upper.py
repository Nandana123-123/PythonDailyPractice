sen=input("Enter a String: ")
b=''
for ele in sen:
    if 'a'<=ele<='z':
        upper=chr(ord(ele)-32)
        b+=upper
    else:
     b+=ele
print("sentence become :",b)
