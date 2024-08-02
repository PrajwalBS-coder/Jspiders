num = 2
n1=(str(bin(num))[2::])
print(bin(num),n1)
n2=''
for i in range(len(n1)):
    if n1[i]=='1':
        n2+='0'
    else:
        n2+='1'
n2+=' '
print(int(n2,2))