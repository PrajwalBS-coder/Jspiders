s="we ArE gOOd In sOmE OnEs stOry"
vowels="aeiouAEIOU"
res=""
for i in range(len(s)):
    if(s[i] in vowels):
        res+=s[i]
    
print(res)