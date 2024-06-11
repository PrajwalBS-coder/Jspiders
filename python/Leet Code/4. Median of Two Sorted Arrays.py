nums1 = [4,5,6,8,9]
nums2 = []
l=nums1+nums2
m=0
l.sort()
print(l)
if(len(l)%2==0 and len(nums1) !=0 and len(nums2)!=0):
    print("1st")
    print(l[len(l)//2],l[(len(l)//2)-1])
    m=(l[len(l)//2]+l[(len(l)//2)-1])/2
elif(len(nums1)==0):
    m= sum(nums2)/len(l)

elif(len(nums2)==0 and len(l)%2!=0):
    m=l[len(l)//2]
elif(len(nums2)==0):
    print("emp num2")
    m=sum(nums1)/len(l)
else:
    m=l[len(l)//2]
print(m)