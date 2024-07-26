with open("test.txt") as f:
    l=f.readlines()
    # print(l)
    c=0
    l=[i.strip('\n') for i in l]
    for i in l:
        c+=len(i)
    print(l,c)