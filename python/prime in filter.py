def is_prime(n):
    for fa in range(2,n//2+1):
        if n%fa==0:
            return False
    return True
print(len((list(filter(is_prime,range(100,1000))))))