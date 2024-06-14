s = "paper"
t = "title"
l=[]
for i in range(len(s)):
    l.append(ord(s[i])-ord(t[i]))
print(l)