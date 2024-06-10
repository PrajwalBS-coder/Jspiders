import copy
heights = [5,1,2,3,4]
l=copy.copy(heights)
l.sort()
#print(heights,l)
print(len([i for i in range(len(heights)) if heights[i]!=l[i]]))