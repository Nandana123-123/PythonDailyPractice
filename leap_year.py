n=5                          #int(input("Enter a number"))

for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=" ")

        else:
            print(" ",end=" ")
    print()