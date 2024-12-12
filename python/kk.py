def amax(a):
    m=max(a)
    a.remove(m)
    return max(a)
print(amax([12,30,50,70,60,55]))