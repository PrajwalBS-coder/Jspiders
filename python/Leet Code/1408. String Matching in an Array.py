words =["mass","as","hero","superhero"]
a=[]
for word in words:
    for i in words:
        if word in i and word!=i:
            a.append(word)
            break
print(a)