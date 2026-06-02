from itertools import *

data=[x for x in input("Enter a number: ").split()]
n=int(input("Enter a number for the rotations: "))
lst=list(permutations(data,n))
for ele in lst:
    print("".join(ele))