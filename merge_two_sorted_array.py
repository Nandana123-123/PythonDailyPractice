def merge(nums1, m, nums2, n):
    for i in range(n-1):
        nums1[m+i]=nums2[i]

    nums1.sort()

nums1=[int(x) for x in input("Enter the first sorted array: ").split()]
m=int(input("Enter the number of elements in the first array: ")) 
nums2=[int(x) for x in input("Enter the sec sorted array: ").split()]
n=int(input("Enter the number of elements in the sec array: "))
merge(nums1,m,nums2,n)


