dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
l=sentence.split()
for i in range(len(l)):
    for j in range(len(dictionary)):
        if(dictionary[j][0][1] in l[i][0][1]):
            l[i]=dictionary[j]
print(l)