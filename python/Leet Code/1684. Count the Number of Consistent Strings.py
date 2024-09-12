allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
c=0
for i in words:
    if(all(c in allowed for c in i)):
        c+=1

print(c)