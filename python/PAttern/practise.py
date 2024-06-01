line=4
for row in range(1,line+1):
    for col in range(1,line+1):
        if(row==0 or col==0 or row==line-1 or col==line-1 or row==col==line-1 or row==col==line//2):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()