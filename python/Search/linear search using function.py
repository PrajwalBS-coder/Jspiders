def linear(l,searchitem):
    for i in range(len(l)):
        if l[i]==searchitem:
            return i
            break
    else:
        return -1



l=[3,6,22,5,8,9,0,34,54]
serachite=int(input("Enter Search "))
print(linear(l,serachite))
