s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
l=set()
l2=set()
for i in range(len(s)-9):
    if(s[i:i+10] not in l and s[i:i+10] in l2):
        l.add(s[i:i+10])
    else:
        l2.add(s[i:i+10])
print(l)