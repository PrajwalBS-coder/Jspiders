costs = [1,6,3,1,2,5]
coins = 20
c=0
costs.sort()
for i in range(len(costs)):
    if coins >= costs[i]:
        coins = coins - costs[i]
        c+=1
print(c)