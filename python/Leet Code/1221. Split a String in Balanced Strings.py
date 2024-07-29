s = "RLRRLLRLRL"
for i in range(len(s)):
    for j in range(i,len(s)):
        l=s[i:j]
        if(l.count('R')==l.count('L')):
            print(s[i:j])