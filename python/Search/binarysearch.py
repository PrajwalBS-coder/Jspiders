l=[3,6,22,5,8,9,0,34,54]
searchitem=int(input())
l.sort()
print(l)
low=0
high=len(l)-1
while(low<=high):
    mid=(low+high)//2
    if(l[mid]>searchitem):
        high=mid-1
    elif(l[mid]<searchitem):
        low=mid+1
    elif(searchitem==l[mid]):
        print(mid)
        break
else:
    print(-1)