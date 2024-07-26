import re as r
s="Hello Iam prajwal AMin"
print(r.match('a',s))#if the search string is there in the starting then it'll give match object otherwise None
print(r.search('a',s))#it'll give 1st occurance of a search pattern
print(r.findall('a',s))#it'll return the list containing all the matched patterns else empty list([])