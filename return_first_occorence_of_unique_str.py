def first_unique(s):
    t=s.replace(" ","")
    for ele in t:
        if t.count(ele)==1:
            return ele

    return False

s=input("enter a string: ")
t=first_unique(s)
if t:
    print("unique element is: ",t)
else:
    print("unique element is not found")