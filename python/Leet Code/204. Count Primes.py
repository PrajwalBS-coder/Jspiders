n = 10
l=[]
def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
for i in range(2,n):
    if(prime(i)):
        l.append(i)
print(l)
print(prime(4))
