position = [1,2,3,4,5,6,7,8,9,10]
position.sort()
m =4 
l, r = 1, position[-1] - position[0]
ans = -1
while l <= r:
    mid = l + (r - l) // 2
    last_position, balls = position[0], 1
    for i in range(1, len(position)):
        if position[i] - last_position >= mid:
            last_position = position[i]
            balls += 1
    if balls >= m:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print( ans)