def con(arr):
    for i in range(len(arr)-2):
        #print(arr[i],arr[i]+1,arr[i]+2)
        #print(i%2==1),((i+1)%2==1),((i+2)%2==1)
        if(arr[i]%2==1) and ((arr[i+1])%2==1) and ((arr[i+2])%2==1):
            return True
    return False
arr = [1,2,34,3,4,5,7,23,12]
print(con(arr))

