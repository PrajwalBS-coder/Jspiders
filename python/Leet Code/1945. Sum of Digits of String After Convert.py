s = "iiii"
k= 1
con=''

for i in s:
    con+=str(ord(i)-96)
print(con)
# for i in con:
#     re+=int(i)
for j in range(k):
    re=0
    for i in con:
        re+=int(i)
    con=str(re)
print(re)
