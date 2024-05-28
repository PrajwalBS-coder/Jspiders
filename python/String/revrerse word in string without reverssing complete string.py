s="we are good in some ones story"
l=[]
rev=""
for i in range(len(s)):
 
    if(s[i]==" "):
        l.append(rev)
        rev=""
    else:
        rev=s[i]+rev
print(" ".join(l))
