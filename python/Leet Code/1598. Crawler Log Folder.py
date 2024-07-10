logs = ["vv1/","../","./"]
c=0
for i in range(len(logs)):
    logs[i] =logs[i][1:]
    logs[i] =logs[i].strip("/")
    if(logs[i]==".."):
        c-=1
    elif(logs[i]=='.'):
        c-=1
    else:
        c+=len(logs[i])

print(c)
