l=[10,60,75,100,112,115,150]
l.sort()
print(l)
low=0
high=len(l)-1
search=int(input("ENter a no"))
while low<=high and l[low]<=search<=l[high]:
    ind=int(low+ ((low-high)/(l[low]-l[high]))*(search-l[low]))#edited the equation by me it's acutally low-high
    #print(ind)
    if(l[ind]>search):
        high=ind-1
    elif(l[ind]<search):
        low=ind+1
    elif(l[ind]==search):
        print(ind)
        break
    
else:
    print("-1")