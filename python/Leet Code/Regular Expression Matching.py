import re
s = "aa"
p = "a*"
if("*" in p):
    p=p.replace("*","")
    p=p*len(s)
l=re.findall(s,p)
print(l)
if(l):
    print("Yes")
else:
    print("No")