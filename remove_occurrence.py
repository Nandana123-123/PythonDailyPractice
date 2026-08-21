def remove_chr(s):
    res=""
    for ch in s:
        if ch not in res:
            res+=ch
    print(res)

s=input("Enter a string: ")
remove_chr(s)