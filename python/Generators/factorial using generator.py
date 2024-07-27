def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
o1=fac(5)
print(next(o1)) # prints 1
print(next(o1)) # prints 1
print(next(o1)) # prints 1
print(next(o1)) # prints 1
print(next(o1)) # prints 1
print(next(o1)) # prints 1