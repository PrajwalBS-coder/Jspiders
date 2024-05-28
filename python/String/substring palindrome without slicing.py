s="sms"
for sv in range(0,len(s)):
    
    for ev in range(sv+1,len(s)+1):
        word=''
        for ind in range(sv,ev):
            word+=s[ind]    
        for i in range(len(word)):
          rev=""
       # print(word)
        for ind in range(len(word)-1,-1,-1):
           rev+=s[ind]
           #print(rev,end=" ")
        #print(word,rev)
        if(word==rev):
            print(word)
            
