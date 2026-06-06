strs=input("Enter a words: ").split()
d={}
for word in strs:
    key="".join(sorted(word))
    if key not in d:
        d[key]=[]
    d[key].append(word)

print(list(d.values()))