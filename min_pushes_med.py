from collections import Counter

def minimumPushes(word):
    freq = sorted(Counter(word).values(), reverse=True)

    ans = 0
    for i, f in enumerate(freq):
        ans += f * (i // 8 + 1)

    return ans

word=input("Enter a word: ")
print("Minimum pushes required:", minimumPushes(word))