var=5
for inn in range(1,var+1):
    for sp in range(var-inn):
        print(" ",end=" ")
    for val in range(inn):
        if inn==5 or val==inn-1 or val==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
print("*********************REVERSE OF THI ONE************************")
print()

for inn in range(var,0,-1):
    for sp in range(var-inn):
        print(" ",end=" ")
    for val in range(inn):
        if(val==0 or val==inn-1 or inn==var):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()