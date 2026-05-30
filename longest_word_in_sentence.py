sen=input("Enter a sentence: ")
words=sen.split()
large=" "
for ele in words:
    if len(ele)>len(large):
        large=ele

print("longest word is: ",large)