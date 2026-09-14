n=int(input("Enter a number: "))
nums=[10]
i=10
while i<len(str(n)):
    if n%i==0:
        nums.append(i)
    i*=10

print("last number divisible by 10 is: ",nums[len(nums)-1])
