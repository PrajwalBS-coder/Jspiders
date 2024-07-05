n=5
sp=4
for i in range(2,n+2):
    for s in range(sp):
        print(" ",end=" ")
    for val in range(1,i):
        print(val,end=" ")
    print()
    sp-=1