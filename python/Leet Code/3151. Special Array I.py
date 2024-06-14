def sp(l):
    for i in range(len(l)-1):
        if(l[i]%2==l[i+1%2]):
            return False
            
    return True

l=[1]
print(sp(l))