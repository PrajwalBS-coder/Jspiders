def odd(n):
    for val in range(1,n+1):
        if(n%2==0):
            return "Even"
        return "Odd"
print(list(map(odd,range(1,9))))