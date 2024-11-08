capacity=4
val=[6,3 ,8 ,6 ,9 ,8 ,2 ,4 ,10 ,9]
wt=[2 ,1 ,3 ,1 ,4 ,1 ,2 ,2, 5, 7]
oprofit=0
for i in range(len(val)):
    ipprofit=0
    if(wt[i]<=capacity):
        ipprofit+=val[i]
        capacity-=wt[i]
        if(ipprofit>oprofit):
            oprofit=ipprofit
print(oprofit)