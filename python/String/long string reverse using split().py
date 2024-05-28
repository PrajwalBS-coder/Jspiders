s="we are good in some ones story"
words=s.split()
#print(words,type(words))
l=[]

for i in range(len(words)-1,-1,-1):
    l.append(words[i])
#print(" ".join(l))


# all the above code in single line
print(" ".join([s.split() [i] for i in range(len(s.split())-1,-1,-1)]))
