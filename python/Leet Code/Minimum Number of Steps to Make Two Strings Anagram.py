s = "bab"
t = "aba"
c=0
s1=list(s)
t1=list(t)
print(s1,t1)
for ind in range(len(s1)-1):
    if(s1[ind]not in t1):
         c+=1
         print(s1)
    else:
        s1.remove(s1[ind])
        
        print(s1)
print(c)
        

                    
