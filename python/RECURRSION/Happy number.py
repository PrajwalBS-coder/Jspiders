def sqr(n):
    if n==0:
        return 0
    return (n%10)**2+sqr(n//10)

def digit(n):
    if n<=9:
        return n
    
    return digit(sqr(n))

n=digit(9)
print('Happy no' if n==1 or n==7 else 'Not Happy No')
