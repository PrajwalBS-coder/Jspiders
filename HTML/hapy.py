n=20
while(n>9):
    s=0
    while (n!=0):
        e=n%10
        s+=e*e
        n=(n//10)
    n=s
if(n==1) or (n==7):
   print('happy')

else:
    print("Not happy")