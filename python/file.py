with open("test.txt") as f:
    l=f.readline()
    l=[i.strip('\n') for i in l]
    print(l)