s="cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"
l=[]
max=0
ele=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j:])
print(l)
for i in l:
    if l.count(i)>=3:
        if(len(i)>max):
            max=len(i)
            ele=i
print(len(ele),ele)
print(l.count('ee'))
        