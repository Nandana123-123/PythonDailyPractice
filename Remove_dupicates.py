#way-01
#to remove duplicates from a list  without using built in

lst=[int(x) for x in input("Enter a array elements: ").split()]
dupicated=[]
not_duplicated=[]

for ele in lst:
    if not ele in dupicated:
        not_duplicated.append(ele)
    #else:
     #   dupicated.append(ele)

#print("duplicated elements are: ",list(set(dupicated)))
print("non duplicated elements are: ",list(set(not_duplicated)))


print("\n")
print("**********************************************************")
print("\n")

#way-02
#to remove duplicates from a list  by using set()
lst=[int(x) for x in input("Enter a array elements: ").split()]
uniqe_ele_list=list(set(lst))
print("unique elements are: ",uniqe_ele_list)

print("\n")
print("**********************************************************")
print("\n")

#way-03
#to remove duplicates from a list using dictionary

lst=[int(x) for x in input("Enter a array elements: ").split()]
not_dup={}
seen={}
for ele in lst:
    if ele in not_dup:
        seen[ele]=seen.get(ele,0)+1
    else:
        not_dup[ele]=not_dup.get(ele,0)+1

non_dup=[]
seened=[]
for k in not_dup.keys():
    non_dup.append(k)
for k in seen.keys():
    seened.append(k)

print("duplicated elements are: ",seened)
print("non duplicated elements are: ",non_dup)

print("\n")
print("**********************************************************")
print("\n")

#way-03
#to print only the non repeating elements in the list

lst=[int(x) for x in input("Enter a array elements: ").split()]

unique_ele=[]
for ele in lst:
    if lst.count(ele)==1:
        unique_ele.append(ele)

print("unique elements are: ",unique_ele)

print("\n")
print("**********************************************************")
print("\n")
#way 4 to remove duplicates in sorted array and return the length of a non duplicated array

def removeDuplicates(nums):
    n=len(nums)
    if n==0:
        return 0
    j=0
    for i in range(n):
        if nums[i]!=nums[j]:
            j+=1
            nums[j]=nums[i]

    return j+1


nums=[int(x) for x in input("Enter a numbers for a list:").split()]
print(removeDuplicates(nums))