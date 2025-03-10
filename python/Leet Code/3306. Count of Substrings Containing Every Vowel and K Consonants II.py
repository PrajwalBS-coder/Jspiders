from itertools import combinations
word = "ieaouqqieaouqq"
k = 1
op=[]
v='aeiou'

l= [word[i:j] for i, j in combinations(range(len(word) + 1), 2)]
print(l)
for i in l:
    if v in i and len(set(i))==len(v)+k:
        op.append(i)
print(op)