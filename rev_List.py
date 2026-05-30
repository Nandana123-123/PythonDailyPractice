arr=[int(x) for x in input("Enter a array elements: ").split()]
rev=[]
for ele in arr:
    rev=[ele]+rev

print(rev)

#using built in functions

arr=[int(x) for x in input("Enter a array elements: ").split()]
print(arr[::-1])