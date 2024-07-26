import re as r
s="Hello Iam prajwal AMin"
print(r.subn('5','A',s,2))#this one is used to repaklce the existing char with required one,It'll return alterd string as well no.of count that characters get effected
print(list(r.finditer('a',s)))
sp=r.compile('a')
print(r.findall(sp,s))