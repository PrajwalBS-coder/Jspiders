def divide(x,y):
    return x/y
def divi(d):
    return lambda x:divide(x,d)

half1=divi(2)
half2=divi(3)


print(half1(32),half2(32))

print(half1(40),half2(40))