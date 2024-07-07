numBottles = 15
numExchange = 7
consumed_bottles = 0
while numBottles >= numExchange:
    consumed_bottles += numExchange
    numBottles -= numExchange
    numBottles += 1
print(numBottles+consumed_bottles)