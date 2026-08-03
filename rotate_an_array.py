def rve(nums,start,end):
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1

def rotate(nums, k):
    k = k % len(nums)
    n=len(nums)
    rve(nums,0,n-1)
    rve(nums,0,k-1)
    rve(nums,k,n-1)


nums=[int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
start=int(input("Enter the start index: "))
end=int(input("Enter the end index: "))
k=int(input("Enter the number of positions to rotate: "))
rve(nums,start,end) 
rotate(nums, k)