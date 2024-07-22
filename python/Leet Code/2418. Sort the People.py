names = ["Mary","John","Emma"]
heights = [180,165,170]
# heights.sort()
height_to_name_map = dict(zip(heights, names))
# print(height_to_name_map)  
heights.sort(reverse=True)
l=[]
for i in heights:
    if i in height_to_name_map.keys():
        l.append(height_to_name_map[i])
print(l)