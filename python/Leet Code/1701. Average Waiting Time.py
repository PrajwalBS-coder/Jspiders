l=[[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
s=(l[0][0])
op=0
for i in range(len(l)):
    print(l[i][1])
    print(s,op)
    s+=l[i][1]
    if(s>l[i][0]):
        op+=s-l[i][0]
    else:
        s=sum(l[i])
        op+=s-l[i][0]
    print("after cal",s,op)
    # s+=l[i+1][1]
print(op/len(l))