import heapq,math
nums = [10,10,10,10,10]
k = 5
ans = 0
max_heap = [-i for i in nums]
heapq.heapify(max_heap)
while k > 0:
    k -= 1
    max_element = -heapq.heappop(max_heap)
    ans += max_element
    heapq.heappush(max_heap, -math.ceil(max_element / 3))

print( ans)