a='a2b10'
op=''
n=''
for i in range(len(a)-1,-1,-1):
    if('0'<= a[i] <='9'):n=a[i]+n
    if('a'<= a[i] <='z'):
        op=a[i] * int(n)+op 
        n=''
print(op)
# print(int('10'))