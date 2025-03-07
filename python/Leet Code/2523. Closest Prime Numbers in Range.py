left = 10
right = 19
l=[]
distance=0
smallest_pair=[]
for i in range(left,right+1):
    # print(i)
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        l.append(i)
# print(l)
min_pair = [-1, -1]
min_diff = float('inf')

for i in range(len(l) - 1):
    diff = l[i + 1] - l[i]
    if diff < min_diff:
        min_diff = diff
        min_pair = [l[i], l[i + 1]]

print( min_pair)
