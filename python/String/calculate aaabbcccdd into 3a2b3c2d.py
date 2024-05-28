a="aaabbcccdd"
c=1
re=""
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c+=1
    else:
        re+=a[i]+str(c)
        c=1
        print(a[i],c)
re+=a[i]+str(c)
print(re)


#if you wanto add space and do the calculations
a="aaabbcccdd"
a+=" "
c=1
re=""
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c+=1
    else:
        re+=a[i]+str(c)
        c=1
        print(a[i],c)
#re+=a[i]+str(c)
print(re)
