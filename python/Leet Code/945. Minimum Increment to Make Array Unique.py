nums = [3,2,1,2,1,7]
nums.sort()
numTracker = 0
minIncreament = 0

for num in nums:
    numTracker = max(numTracker, num)
    print(numTracker)
    minIncreament += numTracker - num
    print(minIncreament)
    numTracker += 1
    print(numTracker)
    
print(minIncreament)