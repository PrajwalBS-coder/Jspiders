def linear(l,ele,ind=0):
    if ind==len(l):
        return -1
    if(ele==l[ind]):
        return ind
    return linear(l,ele,ind+1)
l=[3,6,22,5,8,9,0,34,54]
serachite=int(input())
print(linear(l,serachite))