p='3 4 21 36 10 28 35 5 24 42'
scores = list(map(int, p.rstrip().split()))
highest = lowest = scores[0]
high_breaks = low_breaks = 0
   # Iterate through scores
for score in scores[1:]:
    if score > highest:  # If a new highest score is found
        highest = score
        high_breaks += 1
    elif score < lowest:  # If a new lowest score is found
        lowest = score
        low_breaks += 1
print(high_breaks,low_breaks)