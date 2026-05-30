s1=input("Enter a String: ")
s2=input("Enter a String: ")
if len(s1)==len(s2) and sorted(s1.replace(" ","").lower())==sorted(s2.replace(" ","").lower()):
    print("both sentences are anagrams")
else:
    print("Not an anagrams")
