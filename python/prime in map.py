def prime(n,c=0):
    for val in range(1,n+1):
        if(n%val==0):
            c+=1
    if(c==2):
        return "Prime"
    return "Not Prime"

print(list(map(prime,range(10,51))))