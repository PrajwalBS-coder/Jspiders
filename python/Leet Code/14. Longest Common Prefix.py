strs = ["flower","flow","flight"]
i=0
s=''
while(i<len(strs[0])):
    for j in range(len(strs)):
        if i>len(strs[j]) and strs[0][i] not in strs[j]:
            print(s)
            break
        else:
            s+=strs[0][i]
    i+=1
# print(s)