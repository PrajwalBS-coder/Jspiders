blocks = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW"
k = 15
c=0
# print(k*("W"))
if k*('B') in blocks:
    print("No need")
for i in range(len(blocks)):
    if blocks[i] == "W" and i<k:
        c+=1
        print(c,i)
print(c)