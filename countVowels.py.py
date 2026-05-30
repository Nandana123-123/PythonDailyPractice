string=input("Enter a string: ")
vow="aeiou"
vowel={}
for ele in string:
    if ele in vow:
        vowel[ele]=vowel.get(ele,0)+1

print(vowel)