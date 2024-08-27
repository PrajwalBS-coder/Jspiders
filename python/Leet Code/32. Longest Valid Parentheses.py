s =  ""

ob=0
cb=0
for i in s:
    if i=='(':
        ob+=1
    if i==')':
        cb+=1
print(abs(ob-cb)*2)