s = "111111"
c=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if("0" not in s[i:j]):
            # print(s[i:j])
            c+=1
print(c)