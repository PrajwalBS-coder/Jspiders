arr=[0,1,1,1,0,1,1,0,1]
ones = 0
n = len(arr)
for i in range(n):
    for j in range(i, n):
        # print(arr[i:j+1])
        c=(arr[i:j+1]).count(1)
        if set(arr[i:j+1]) == 1:
            c=-1
        if c>ones:ones=c
print(ones)