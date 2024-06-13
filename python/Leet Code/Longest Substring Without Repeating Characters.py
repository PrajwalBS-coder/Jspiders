s = "pwwkew"
l=[]
for i in range(len(s)):
    for j in range(i,len(s)+1):
        print(s[i:j+1])
        l.append(list(set(s[i:j+1])))
print(l)