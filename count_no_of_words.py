sen=input("Enter a string: ")
spl=sen.split()
print(len(spl))

#method 2
sen=input("Enter a string: ")
count=1
for ele in sen:
    if ele==" ":
        count+=1
print(count)
