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


#method 3
sen=input("Enter a sentence: ")
spl=sen.split()
sum=0
for i in range(len(spl)):
    sum+=1
print(sum)