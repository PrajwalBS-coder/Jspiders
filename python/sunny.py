def sunny(n,sq=0):
    while(sq**2<=n+1):
        if(sq**2==n+1):
            return True
        sq+=1
    return False
n=15
print("Sunny Number" if(sunny(n)) else "Not Sunny Number")