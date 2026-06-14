from itertools import permutations

sen=input("Enter a string: ")
n=int(input("Enter length of word: "))
per=list(permutations(sorted(sen),n))
for ele in per:
    print(" ".join(ele))