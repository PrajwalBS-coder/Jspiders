def numbers(n):
    print(n,end =" ")
    if(n==10):
        return 
    numbers(n+1)

n=1
numbers(n)