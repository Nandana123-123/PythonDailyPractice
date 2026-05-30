def palindrome(s):
    t=s.lower()
    left=0
    right=len(t)-1

    while(right>=left):
        if t[left]==" ":
            left+=1
        if t[right]==" ":
            right-=1

        if t[left]!=t[right]:
            return False

        left += 1
        right -= 1
        return True


s=input("Enter a string: ")
p=palindrome(s)

if p:
    print("String is palindrome")
else:
    print("String is not palindrome")

print()
print("********************************************")
print()

#using built in methods like index sclicing

s=input("Enter a string: ")
if s==s[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

