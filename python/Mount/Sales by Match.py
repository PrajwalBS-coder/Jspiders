n=7
arr=[1,2,1,2,1,3,2]
arr.sort()
c=0
i=0
while i< len(arr)-1:
    if arr[i]==arr[i+1]:
        c+=1
        arr.pop(i)
        arr.pop(i)
    else:
        i+=1
        # arr.remove(arr[i+1])
print(c)