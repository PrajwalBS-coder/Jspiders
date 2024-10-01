arr = [3,8,17,2,5,6]
# arr.sort()
k = 10
a1=arr[:len(arr)//2:]
a2=arr[len(arr)//2::]
for i in a1:
    for j in a2:
        if (i+j)%k==0:
            print(i,j,True)
            break
else:
    print(False)

print(a1,a2)
