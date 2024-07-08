n = 5
k = 2
f = list(range(1, n+1))
cp = 0#current position
while n > 1:
    cp = (cp + (k-1)) % n
    f.pop(cp) 
    n -= 1
print( f[0])