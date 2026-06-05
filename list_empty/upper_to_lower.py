sen=input("Enter a String: ")
b=''
for ele in sen:
    if 'A'<=ele<='Z':
        lower=chr(ord(ele)+32)
        b+=lower
    else:
        b+=ele
print("sentence become :",b)