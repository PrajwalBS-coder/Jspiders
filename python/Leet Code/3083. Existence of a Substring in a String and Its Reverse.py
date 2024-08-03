s = "ausoee"
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if(len(s[i:j])>=2):
            l.append(s[i:j])
# print(l)
s2=s[::-1]
# print(s2)
for i in range(len(l)):
    if l[i] in s2:
        print(l[i])
        break
print(l)
