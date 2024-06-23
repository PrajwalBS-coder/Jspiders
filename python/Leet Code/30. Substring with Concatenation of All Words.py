"""s= "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

w="".join(words[::-1])
w1="".join(words)
if(s):
    if(w1 in s):
        l.append(s.find(w))
    if(w in s):
        l.append(s.find(w1))
print(l,w,w1)"""
import itertools
s="aaaaaaaaaaaaaa"
words =["aa","aa"]
l=[]
p=(list((itertools.permutations(words))))
print(p)
for i in range(len(p)):
    w="".join(p[i])
    if(w in s):
        c=s.count(w)
        print(c)
        l.append(s.find(w))
        if(c>=1):
            l.append(s.find(w,s.find(w)+1))
        
l=list(set(l)) 
l=list(filter(lambda x: x >= 0, l))      
l.sort()
print(l)