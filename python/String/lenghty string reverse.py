s="we are good in some ones story"
res=""
rev=[]
for i in range(len(s)-1,-1,-1):
    if(s[i]==" "):
        rev.append(res)
        res=""
    else:
        res=s[i]+res
#
rev.append(res)

print(" ".join(rev))
