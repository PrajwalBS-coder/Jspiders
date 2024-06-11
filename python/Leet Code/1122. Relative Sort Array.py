arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
re=[]
for i in range(len(arr2)):
    for j in range(len(arr1)):
        if(arr2[i]==arr1[j]):
            re.append(arr1[j])
            #arr1.remove(arr1[j])
l=[i for i in arr1 if i not in re]
#print(l)
l.sort()
[re.append(l[i]) for i in range (len(l))]
print(re)

