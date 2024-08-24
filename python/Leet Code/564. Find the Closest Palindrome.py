n = "123"
c1,c2=0,0
l=[]
l2=[]
for i in range(int(n)-1,-1,-1):
    c1+=1
    if(str(i)==str(i)[::-1]):
        # print(i)
        l.append(str(i))
        # c1+=1
        break
# k=int(n)
# while(len(l2)!=1):
#     if(str(k)==str(k)[::-1]):
#         # print(k)
#         l2.append(str(k))
#         c2+=1
#         k+=1
for i in range(int(n)+1,int((n)*2)+1):
    c2+=1
    if(str(i)==str(i)[::-1]):
        # print(i)
        l2.append(str(i))
        break
print(c1,c2,l,l2)
if(c1==c2):
    print("".join(l))
elif(c1>c2):
    print("".join(l2))
else:
    print("".join(l))