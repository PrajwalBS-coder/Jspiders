s1 = "this apple is sweet"
s2 = "this apple is sour"
l1=s1.split()
l2=s2.split()
l3=[]
l4=[]

# l3.append(str(set(l1)-set(l2)))
# l3.append(str(set(l2)-set(l1)))
# print(l3)
l3=l1+l2
for i in l3:
    if l3.count(i)==1:
        l4.append(i)
print(l4)