
#by using built in
word=input("Enter a word: ")
fre={}
for ele in word.replace(" ",""):
    fre[ele]=fre.get(ele,0)+1

print(fre)




#without using built in
word=input("Enter a word: ")
fre={}
for ele in word.replace(" ",""):
    if ele in fre:
        fre[ele]+=1
    else:
        fre[ele]=1
print(fre)


