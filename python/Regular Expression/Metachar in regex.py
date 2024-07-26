import re as r
s="Hello Iam pr@jwal B.$ \nAMin"
print(r.findall('.',s))#lists every character in list excluding "\n"
print(r.findall('^He',s))#it works like starts with o/p will be in list if given pattern exist else [] empty list
print(r.findall('n$',s))#it works like ends with o/p will be in list if given pattern exist else [] empty list
print(r.findall('H*o',s))