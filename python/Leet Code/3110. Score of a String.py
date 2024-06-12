s = "zaz"
sum=0
for i in range(len(s)-1):
    sum+=abs(ord(s[i])-ord(s[i+1]))
    print(s[i])
print(sum)