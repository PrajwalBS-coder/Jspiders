def bi(n,res=0,pos=1):
    while(n!=0):
        res+=(n%2)*pos
        
        pos*=2
        
        n//=10
       
    return res
print(bi(100))
