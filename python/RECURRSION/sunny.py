def sunny(num,n=0):
    if(n*(n+1)!=num):
        sunny(n+1)

    return False
        
    
print('Pronic' if sunny(111) else "Not Pronic")