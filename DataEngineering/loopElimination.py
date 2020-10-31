#Benefits of eliminating loops
# Fewer lines of code
# Better code readability
# Efficiency gains

import numpy as np

mat = [
    [23,53,76,12],
    [91,34,64,25],
    [87,65,20,72]
]

#calculating sum of each row and adding them to list

total_comp = [sum(row) for row in mat]
print("List comprehension output: ",total_comp)

total_map = [*map(sum,mat)]
print("map output: ",total_map)

matnp = np.array(mat)
numpysum=matnp.sum(axis=1)
print("Numpy sum output: ",numpysum)

# output
# List comprehension output:  [164, 214, 244]
# map output:  [164, 214, 244]
# Numpy sum output:  [164 214 244]