def numbers(n):
    if(n>10):
        return
    print(n,end=" ")
    numbers(n+1)
n=1
numbers(n)