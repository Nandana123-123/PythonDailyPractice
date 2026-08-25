def findMedianSortedArrays(nums1, nums2):
    num=[]
    for i in range(len(nums1)):
        num.append(nums1[i])

    for i in range(len(nums2)):
        num.append(nums2[i])

    num.sort()

    mid=(len(num))//2
    if(len(num)%2!=0):
        return num[mid]

    return (num[mid-1]+num[mid])/2.0


nums1=[int(x) for x in input("Enter the element of the array separated by space: ").split()]
nums2=[int(x) for x in input("Enter the element of the array separated by space: ").split()]
print(findMedianSortedArrays(nums1,nums2))