matrix = [[3,6],[7,1],[5,2],[4,8]]
l=[]
k=[]
for i in range(len(matrix)):
    l.append(min(matrix[i]))
k.append((max(l)))
print(k)