n=5
for inn in range(n):
    for sp in range(n-inn):
        print(" ",end=" ")
    for val in range(2*inn+1):
        if val==0 or inn==n-1 or val==inn*2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
print("**************************************************************")
print()
for inn in range(n-1,-1,-1):
    for sp in range(n-inn):
        print(" ",end=" ")
    for val in range(2*inn+1):
        if val==0 or inn==n-1 or val==inn*2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()