s ="leetcode"
v='aeiou'
l=[]
for i in range(len(s)):
    if s[i] in v:
        l.append(s[i])
l.reverse()
li=0
ss=list(s)
for i in range(len(ss)):
    if ss[i] in v:
       ss[i]=l[li]
       li+=1
print("".join(ss))