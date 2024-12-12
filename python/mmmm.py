stre=['flower','flow','flight']
s=''
for i in stre[1]:
    for j in range(1,len(stre)-1):
        if i in stre[j] and i in stre[j+1]:
            s+=i
print(s)
