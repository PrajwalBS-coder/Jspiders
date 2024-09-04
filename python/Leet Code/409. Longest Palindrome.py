s = "abccccdd"
l=[]
for i in range(len(s)+1):
    for j in range(i,len(s)):
            if(s[i:j]==s[i:j][::-1]):
                  l.append(s[i:j])
print(l)