# import numpy as np

# arr = np.array((1, 2, 3, 4, 5))


# print(arr)
from collections import Counter
d={1:2,3:4,5:6}
d2={"1":2,"3":4,"5":6}
d3=Counter(d)+Counter(d2)
print(d3)