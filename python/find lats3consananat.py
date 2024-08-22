n=int(input())
s=''
c=22
for i in range(n):s+=input()
s=s[::-1]
for i in s:
    if(c==0):
        if i not in 'aeiou':
            print(i)
            break
    if i not in 'aeiou':
        c-=1
print(s)
print('a'*5)