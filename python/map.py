def rev(n,newnum=0):
    while(n!=0):
        ld=n%10
        newnum=(newnum*10)+ld
        n//=10
    return newnum
print(list(map(rev,range(100,151))))#for reversing no within the range of 100-150