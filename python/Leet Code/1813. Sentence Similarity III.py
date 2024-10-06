s1 = "CwFfRo regR"
s2 = "CwFfRo H regR"
l1=s1.split()
l2=s2.split()
if(len(s2)>len(s1)):
    print(False)
else:
    for i in l2:
        if i not in l1:
            print(False)

    print(True)
# print(l2 in l1)