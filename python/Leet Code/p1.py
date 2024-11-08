def fun(arr):
    max=-1
    for i in range(len(arr)):
        # print(arr[i::])
        # insum=sum(arr[::])
        # print(max)
        # print(insum)
        # if(insum>max):
        #     max=insum
        for j in range(i,len(arr)+1):
            print(arr[i:j:])
            insum=sum(arr[i:j:])
            print(max)
            print(insum)
            if(insum>max):
                max=insum
    return max
# nums=[-2,1,-3,4,-1,2,1,-5,4]
nums=[-1]
# nums=[5,4,-1,7,8]
print(fun(nums))
print(sum([-1,0]))