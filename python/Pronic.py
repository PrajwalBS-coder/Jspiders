def pronic(n,pro=0):
    while(pro*(pro+1))<=n:
        if (pro*(pro+1))==n:
            return True
        pro += 1
    return False

n=111
print('Pronic Number' if(pronic(n)) else "Not Pronic Number")