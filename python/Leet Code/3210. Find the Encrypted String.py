s = "aaa"
k = 1
p=s*(k+1)
print(s)
op=''
for i in range(len(s)):
    op+=p[i+k]
print(op)

