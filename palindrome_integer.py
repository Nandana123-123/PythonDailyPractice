def isPalindrome(x):
    if x <0:
        return False

    temp=x
    rev=0
    while x>0:
        rem=x%10
        rev=rev*10+rem
        x=x//10

    return rev==temp

x=int(input("Enter a number: "))
print(isPalindrome(x))