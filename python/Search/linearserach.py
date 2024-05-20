l=[3,6,22,5,8,9,0,34,54]
serachitem=int(input())
for i in range(len(l)):
    if l[i]==serachitem:
        print(i)
        break
else:
    print(-1)