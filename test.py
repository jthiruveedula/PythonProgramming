from timeit import timeit
from datetime import datetime
import numpy as np
start = datetime.now()


nums = np.random.rand(1000)
print(nums)

print(datetime.now() - start)

