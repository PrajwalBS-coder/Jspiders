var=5
sp=var-1
for v in range(var-1,-1,-1):
    for d in range(sp):
        print(" ",end=" ")
    for k in range(5,v,-1):
        print(k,end=" ")
    print()
    sp-=1
   