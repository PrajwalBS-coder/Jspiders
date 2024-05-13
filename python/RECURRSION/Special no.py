def fact(n):
    if n == 0 or n==1: return 1
    return n*fact(n-1)
def digit(n):
    if n==0:
        return 0
    return fact(n%10)+digit(n//10)

def is_special(n):
    return n==digit(n)

print('Special no' if(is_special(40585)) else 'Not Special No')