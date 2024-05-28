s="POP"
rev=""
res=''
for c in s:
    rev=c+rev
print('palindrrome'if rev==s else 'not palindrome')

for ind in range(-1,-(len(s)+1),-1):
    res+=s[ind]

print(s==res)