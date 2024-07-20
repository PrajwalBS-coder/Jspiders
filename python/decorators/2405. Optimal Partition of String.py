s = "abacaba"
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(len(s[i:j])==len(set(s[i:j]))):
            l.append(s[i:j])
print(l)