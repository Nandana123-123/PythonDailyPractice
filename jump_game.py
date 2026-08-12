def jump(nums):
    jum=0
    en=0
    farthest=0

    for i in range(len(nums)-1):
        if i+nums[i]>farthest:
            farthest=i+nums[i]

        if i==en:
            jum+=1
            en=farthest

    return jum

nums=[int(x) for x in input("Enter a number:").split()]
print(jump(nums))