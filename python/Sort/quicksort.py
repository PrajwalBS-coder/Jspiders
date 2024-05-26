def quick(var):
    if(len(var)<=1):
        return var
    pivot=var[0]
    low=[var[ind] for ind in range(1,len(var)) if pivot>var[ind]]
    high=[var[ind] for ind in range(1,len(var)) if pivot<=var[ind]]
    return quick(low) + [pivot] + quick(high)

var=[2,44,1,42,-1,66,909]
print(quick(var))