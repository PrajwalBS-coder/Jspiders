nums = [0,4]
k = 5
heap = nums.copy()
heapify(heap)
for i in range(k):
    t = heappop(heap)
    heappush(heap, t + 1)
ans = 1
mod = 1000000007
for i in heap:
    ans = (ans*i) % mod
print(ans)