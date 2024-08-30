import re as r
s="godd goof gooooood goooof go ddd"
print(r.findall('g.*d',s))#0 or more occurance
print(r.findall('g+d',s))# 1 or more occurance
print(r.findall('g.?d',s))