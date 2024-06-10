s = "book"
v='aeiouAEIOU'
c1,c2=0,0
a,b=s[:len(s)//2],s[len(s)//2:]
for ch in a:
    if(ch in v):
        c1+=1
for ch in b:
    if(ch in v):
        c2+=1
print(c1,c2)
