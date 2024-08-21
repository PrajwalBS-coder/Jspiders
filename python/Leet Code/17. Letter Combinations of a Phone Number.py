digits = "23"
l=[]
p=[]
q=[]
digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
for i in digits:
    l.append(i)
for i in l:
    if i in digit_to_letters.keys():
        p.append(digit_to_letters[i])
for i in range(len(p)):
    for j in range(i+1,len(p)):
        for k in range(len(p[i])):
            for l in range(len(p[j])):
                q.append(p[i][k]+p[j][l])
print(q)