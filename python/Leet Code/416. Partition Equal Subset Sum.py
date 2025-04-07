a=[1,5,11,5]
a.sort()
if sum(a)%2==1:
    print(False)
else:
    for i in a:
        if i == a[a.index(i)+1::]:
            print("ko")