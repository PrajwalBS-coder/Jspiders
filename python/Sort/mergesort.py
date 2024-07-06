def c(main,left,right):#c stand for conquer 
    mind,lind,rind=0,0,0
    while(lind<len(left) and rind<len(right)):
        if(left[lind]>right[rind]):#if we change comparison operator to "<" it'll give descending order
            main[mind]=right[rind]
            mind+=1
            rind+=1
        else:
            main[mind]=left[lind]
            mind+=1
            lind+=1
    while(lind<len(left)):
        main[mind]=left[lind]
        mind+=1
        lind+=1
    while(rind<len(right)):
        main[mind]=right[rind]
        mind+=1
        rind+=1

def d(l):#d stand for division
    if(len(l)>1):
        left,right=l[:len(l)//2],l[len(l)//2:]
        d(left)
        d(right)
        c(l,left,right)

l=[3,5,1,77,12,904,12,11,0]
d(l)
print(l)