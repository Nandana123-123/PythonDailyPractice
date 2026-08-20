def canConstruct(ransomNote, magazine):
    f={}
    for ele in magazine:
        f[ele]=f.get(ele,0)+1
    
    for ele in ransomNote:
        if ele not in f or f[ele]==0:
            return False
        f[ele]-=1
    return True

ransomNote=input("Enter a string: ")
magazine=input("Enter a string: ")
print(canConstruct(ransomNote,magazine))