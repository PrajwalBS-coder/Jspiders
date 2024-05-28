s="sms"
for sv in range(0,len(s)):
    
    for ev in range(sv+1,len(s)+1):
        word=''
        for ind in range(sv,ev):
            word+=s[ind]
        rev=""
        #print(word)
        for i in range(len(word)):
            rev=rev+word[i]
       # print(rev)

        if(word==rev):
            print(word)

            
       # print(word)
 