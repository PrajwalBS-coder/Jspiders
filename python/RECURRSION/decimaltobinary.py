def todec(n,pos=1):
    if n==0:
        #print("HRERE")
        return 0
    #print("hello")
    return (n%10)*pos+todec(n//10,pos*2)
n=1001
print(todec(n))