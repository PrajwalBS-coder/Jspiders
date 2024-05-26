var=5
for inn in range(1,var+1):
    for val in range(inn):
        if(val==0 or inn==var or val==inn-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("******************REVERSE OF THIS ONE***************************")

var=5
for inn in range(var,0,-1):
    for val in range(inn):
        if(val==0 or inn==var or val==inn-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()