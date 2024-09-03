chalk = [5,1,5]
k = 22
while(k>min(chalk)):
    for i in chalk:
        if(i-k>0):
            k=k-i
print(k)