s="sms"
for sv in range(0,len(s)):
    
    for ev in range(sv+1,len(s)+1):
        word=''
        for ind in range(sv,ev):
            word+=s[ind]    
        rev=""
        for ind in range(len(word)-1,-1,-1):
           rev+=word[ind]
           #print(rev,end=" ")
        #print(rev)
        if(word==rev):
            print(word)#Completed
            
