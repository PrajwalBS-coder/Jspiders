s="aacabdkacaa"
ma=[]
h=0
ele=""
for i in range(len(s)):
    for j in range(i,len(s)+1):
        w=(s[i:j+1])
        if(w==w[::-1]):
            ma.append((s[i:j+1]))
ele=sorted(ma,key=len)[-1]
print(ele)