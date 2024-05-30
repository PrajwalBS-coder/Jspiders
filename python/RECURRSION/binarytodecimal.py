def tobi(n,pos=1):
    if n==0:
        print("HRERE")
        return 0
    #print("hello")
    return (n%2)*pos+tobi(n//2,pos*10)
n=4
print(tobi(n))