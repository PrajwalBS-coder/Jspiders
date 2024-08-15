strs = [""]
l=[]
for i in range(len(strs)):
    p=[]
    # p.append(strs[i])
    for j in range(len(strs)):
        if sorted(strs[i])==sorted(strs[j]):
            p.append(strs[j])
    l.append(p)
unique_lists = list(set(tuple(x) for x in l))
unique_lists = [list(x) for x in unique_lists]
print(unique_lists)