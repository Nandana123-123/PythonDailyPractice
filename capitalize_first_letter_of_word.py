sen=input("Enter a sentence: ")
word=sen.split()
res=""
for ele in word:
    res=res+ele[0].upper()+ele[1:]+" "


print(res)