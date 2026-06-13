def isPalindrome(s):
    t=""
    for ele in s:
        if ele.isalnum() and ele!=" ":
            t+=ele.lower()
    left=0
    right=len(t)-1
    while right>=left:
        if t[left]==" ":
            left+=1
        if t[right]==" ":
            right-=1
        if t[left]!=t[right]:
            return False
        left+=1
        right-=1
    return True

s=input("enter a string:")
print(isPalindrome(s))