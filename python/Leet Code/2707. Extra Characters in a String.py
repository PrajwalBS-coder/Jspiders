s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
s1=set(''.join(dictionary))
s=set(s)
c=0
print(s,s1)

if (len(s1)>len(s)):
    for i in s1:
        if i not in s:
            c+=1
else:
    for i in s:
        if i not in s1:
            c+=1

print(c)