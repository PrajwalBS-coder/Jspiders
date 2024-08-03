numbers = [2,3,4]
target = 6
l=[]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i]+numbers[j]==target):
            l.append(i+1)
            l.append(j+1)
            break
print(l)
