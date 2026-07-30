def minimumPushes(word):
    n=len(word)
    pushes=0

    for i in range(n):
        pushes+=(i/8)+1

    return pushes

word=input("Enter a word: ")
print("Minimum pushes required:", minimumPushes(word))