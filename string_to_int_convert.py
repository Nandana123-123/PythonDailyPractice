s=input("Enter a String: ")
num=0;
for ele in s:
    num=num*10+(ord(ele)-ord('0'))
print(num)
print(type(num))


#method 2
s=input("Enter a String: ")
num=0
for ele in s:
    num=num*10+int(ele)
print(num)
print(type(num))